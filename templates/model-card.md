# Model card: <model or adapter name>

- **Base model:** <name and version>
- **Method:** LoRA / QLoRA SFT, then DPO (or as used)
- **Training data:** see [data card](data-card.md)
- **Hub link:** <Hugging Face URL>
- **Licence:** must be compatible with the base model's licence

## Intended use

The task, the users, and the deployment setting. What it should not be used for.

## Training details

| Setting | Value |
| --- | --- |
| LoRA rank / alpha | |
| Learning rate / schedule | |
| Epochs / steps | |
| Hardware and GPU hours | |
| Training cost | |

## Evaluation

| Variant | Metric 1 | Metric 2 | p95 latency | Cost / 1k requests |
| --- | --- | --- | --- | --- |
| Base model (prompted) | | | | |
| This model | | | | |

Eval set, size and method (labels or calibrated judge).

## Limitations and risks

Known failure modes, out-of-domain behaviour, and safety findings from red-teaming.

## How to use

```python
# Example: load base model + adapter, or call the vLLM endpoint
```
