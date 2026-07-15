from loop_engineering_kit.self_correction import *

if __name__ == "__main__":
    def generate(prompt, feedback=None): return prompt if not feedback else prompt + " with detail"
    def validate(text):
        score = 1.0 if "detail" in text else 0.5
        return ValidationResponse(ValidationResult.PASS if score >= .85 else ValidationResult.NEEDS_IMPROVEMENT, score, "Add detail")
    print(SelfCorrectionLoop().run(generate, validate, "Explain loops"))
