from(bucket: "study")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "aws")
  |> filter(fn: (r) => r["_field"] =~ /aws_host1_.*/)