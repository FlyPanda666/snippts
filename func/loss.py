import torch


def reference_loss(
    policy_choose_logprob: torch.Tensor,
    policy_reject_logprob: torch.Tensor,
    ref_choose_logprob: torch.Tensor,
    ref_reject_logprob: torch.Tensor,
    beta: float,
    freeze_ref: bool = False,
    label_smoothing: float = 0.0,
):
    pi_logratio = policy_choose_logprob - policy_reject_logprob
    ref_logratio = ref_choose_logprob - ref_reject_logprob
    if freeze_ref:
        ref_logratio = 0
    logits = pi_logratio - ref_logratio
    losses = (
        -torch.nn.functional.logsigmoid(beta * logits) * (1 - label_smoothing)
        - torch.nn.functional.logsigmoid(-beta * logits) * label_smoothing
    )
    choose_reward = beta * (policy_choose_logprob - ref_choose_logprob).detach()
    reject_reward = beta * (policy_reject_logprob - ref_reject_logprob).detach()
    return losses, choose_reward, reject_reward
