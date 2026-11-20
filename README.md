# GPU Node Validator

A Python test harness that checks GPU node health by parsing `nvidia-smi` output and reporting PASS/FAIL for each GPU.

## Why
Before a GPU server goes into service, someone has to confirm it's healthy: are all GPUs visible, are temperatures in range, is the right driver loaded? This harness automates those checks so they're repeatable and can run in CI.

## What it checks today
- GPU temperature against a configurable limit (default 85°C)

## How it works
The harness reads the CSV output of:

```
nvidia-smi --query-gpu=index,name,driver_version,temperature.gpu,memory.used,memory.total,utilization.gpu --format=csv
```

For development without GPU hardware, it runs against mocked sample files in `samples/`:
- `healthy.csv`: all GPUs within limits
- `overheating.csv`: one GPU over the limit, to prove the check fails when it should

The parser skips blank and whitespace-only rows, so malformed tool output doesn't crash a validation run.

## Run it

```
python3 check_gpu.py samples/healthy.csv
python3 check_gpu.py samples/overheating.csv
```

Example output:

```
[PASS] GPU 0 temp 34C
[FAIL] GPU 1 temp 92C (limit 85C)
```

## Roadmap
- [ ] Memory usage and driver version checks
- [ ] pytest test suite
- [ ] GitHub Actions CI on every push
- [ ] Kernel log (dmesg) scan for NVIDIA Xid errors
- [ ] DCGM diagnostics integration
- [ ] Run live against nvidia-smi on real GPU hardware

## Tech
Python 3 (standard library only)
