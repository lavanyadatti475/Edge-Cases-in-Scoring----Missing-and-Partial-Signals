from edge_case_log import EdgeCaseLog

log1 = EdgeCaseLog("audio", "NULL_VALUE")
log2 = EdgeCaseLog("video", "OUT_OF_RANGE")

print(log1)
print(log2)

print(log1.to_dict())