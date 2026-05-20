class TestCaseGenerationSkill:
    def generate_test_cases(self, analysis: dict) -> list[dict]:
        module = analysis["module"]

        if module == "login":
            return [
                {
                    "test_case_id": "TC_LOGIN_001",
                    "title": "Verify valid user login",
                    "priority": "High",
                    "preconditions": ["User should be registered", "Login page should be accessible"],
                    "steps": [
                        "Open login page",
                        "Enter valid username",
                        "Enter valid password",
                        "Click login button",
                    ],
                    "expected_result": "User should be redirected to dashboard",
                },
                {
                    "test_case_id": "TC_LOGIN_002",
                    "title": "Verify invalid user login",
                    "priority": "High",
                    "preconditions": ["Login page should be accessible"],
                    "steps": [
                        "Open login page",
                        "Enter invalid username",
                        "Enter invalid password",
                        "Click login button",
                    ],
                    "expected_result": "Error message should be displayed",
                },
            ]

        return [
            {
                "test_case_id": "TC_GENERIC_001",
                "title": f"Verify {module} functionality",
                "priority": "Medium",
                "preconditions": [],
                "steps": ["Open application", "Perform user action", "Verify result"],
                "expected_result": "Expected result should be displayed",
            }
        ]
