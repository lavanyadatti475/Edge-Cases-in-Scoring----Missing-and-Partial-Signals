from edge_case_log import EdgeCaseLog
from score_result import ScoreResult

logs = [

    EdgeCaseLog("audio", "NULL_VALUE"),

    EdgeCaseLog("video", "OUT_OF_RANGE")

]

result = ScoreResult(

    score=70,

    status="PARTIAL",

    logs=logs,

    confidence="MEDIUM"

)

result.print_result()

print("\nDictionary Output:\n")

print(result.to_dict())