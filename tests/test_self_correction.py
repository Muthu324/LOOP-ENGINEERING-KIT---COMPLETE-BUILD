from loop_engineering_kit import SelfCorrectionLoop, ValidationResponse, ValidationResult

def test_corrects_output():
    def generate(prompt, feedback=None): return "good" if feedback else "bad"
    def validate(value):
        ok=value=="good"
        return ValidationResponse(ValidationResult.PASS if ok else ValidationResult.NEEDS_IMPROVEMENT, 1 if ok else .2, "fix")
    result=SelfCorrectionLoop().run(generate, validate, "task")
    assert result["success"] and result["iterations"] == 2 and result["output"] == "good"
