from app.core.config import settings

try:
    import litellm
except ImportError:
    litellm = None

class LLMService:
    def __init__(self):
        self.provider = settings.LLM_PROVIDER.lower()

    def categorize_ticket(self, subject: str, content: str) -> str:
        """Classify ticket into category: BILLING, TECHNICAL, AUTHENTICATION, GENERAL."""
        text = f"{subject} {content}".lower()
        if any(w in text for w in ["invoice", "charge", "payment", "subscription", "card", "billing"]):
            return "BILLING"
        elif any(w in text for w in ["login", "sso", "password", "token", "auth", "oauth"]):
            return "AUTHENTICATION"
        elif any(w in text for w in ["error", "500", "crash", "bug", "database", "slow", "api"]):
            return "TECHNICAL"
        else:
            return "GENERAL"

    def generate_response(self, subject: str, content: str) -> str:
        """Generate helpful AI support response using configured provider."""
        if self.provider == "mock" or litellm is None or not (settings.OPENAI_API_KEY or settings.ANTHROPIC_API_KEY):
            category = self.categorize_ticket(subject, content)
            if category == "BILLING":
                return (
                    "Hello,\n\nThank you for reaching out regarding your billing query. "
                    "Our finance team has received your request and will review payment records shortly. "
                    "You can also download your invoices under Portal Settings > Billing.\n\nBest regards,\nSupportPulse AI"
                )
            elif category == "AUTHENTICATION":
                return (
                    "Hello,\n\nWe noticed you are experiencing login or authentication issues. "
                    "Please try resetting your password via the self-service portal link, or ensure SAML 2.0 assertions are signed correctly.\n\nBest regards,\nSupportPulse AI"
                )
            elif category == "TECHNICAL":
                return (
                    "Hello,\n\nThank you for bringing this technical issue to our attention. "
                    "Our engineering on-call engineer has been notified and is investigating service health logs.\n\nBest regards,\nSupportPulse AI"
                )
            else:
                return (
                    "Hello,\n\nThank you for contacting support. We have received your inquiry and our team will get back to you within 24 hours.\n\nBest regards,\nSupportPulse AI"
                )
        
        # External LLM provider via LiteLLM if API keys are supplied
        try:
            response = litellm.completion(
                model=settings.MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a professional customer support AI assistant for PulseServe."},
                    {"role": "user", "content": f"Subject: {subject}\n\nIssue: {content}"}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[Offline Fallback] Thank you for your inquiry regarding '{subject}'. Our team is investigating."

llm_service = LLMService()
