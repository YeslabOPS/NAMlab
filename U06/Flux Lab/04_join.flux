cpu1_t = from(bucket: "study")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "dnac")
  |> filter(fn: (r) => r["_field"] == "cpu1")
  |> truncateTimeColumn(unit:5m)

cpu2_t = from(bucket: "study")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "dnac")
  |> filter(fn: (r) => r["_field"] == "cpu2")
  |> truncateTimeColumn(unit:5m)

join(tables: {cpu1:cpu1_t, cpu2:cpu2_t}, on:["_time"])
  |> map(fn: (r) => ({
      _time: r._time,
      _value: (r._value_cpu1 - r._value_cpu2),
      cpu1_ori: r._value_cpu1,
      cpu2_ori: r._value_cpu2
  }))