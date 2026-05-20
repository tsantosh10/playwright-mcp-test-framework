class RequirementAnalysisSkill:
    def analyse(self, requirement: str) -> dict:
        requirement_lower = requirement.lower()

        module = "unknown"
        if "login" in requirement_lower:
            module = "login"
        elif "registration" in requirement_lower:
            module = "registration"
        elif "checkout" in requirement_lower:
            module = "checkout"

        return {
            "module": module,
            "raw_requirement": requirement,
            "possible_actions": self._extract_actions(requirement_lower),
        }

    def _extract_actions(self, text: str) -> list[str]:
        actions = []

        if "enter" in text or "input" in text:
            actions.append("fill")
        if "click" in text or "submit" in text:
            actions.append("click")
        if "verify" in text or "should" in text:
            actions.append("assert")

        return actions
