from loop_engineering_kit import SelfCorrectionLoop, ValidationResponse, ValidationResult

def generator(prompt, feedback=None): return prompt if feedback is None else prompt + " Clear, verified, and complete."
def validator(output):
    score = 0.95 if "verified" in output else 0.6
    return ValidationResponse(ValidationResult.PASS if score >= .85 else ValidationResult.NEEDS_IMPROVEMENT, score, "Add verification")

if __name__ == "__main__": print(SelfCorrectionLoop().run(generator, validator, "Describe loop engineering."))
