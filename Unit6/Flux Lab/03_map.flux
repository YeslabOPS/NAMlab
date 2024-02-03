from(bucket: "study")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "dnac")
  |> filter(fn: (r) => r["_field"] == "cpu1")
  |> map(fn: (r) => ({time: r._time,
              metric: r._field,
              cpu_value: r._value
              }))