import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def show(tokenizer: AutoTokenizer):
    corpus = [
        "loss_fn = torch.nn.CrossEntropyLoss(reduction=, ignore_index=-100)",
        "红藕香残玉簟秋",
    ]
    print(tokenizer(corpus, return_tensors="pt", padding="longest"))
    """
    {'input_ids': tensor([[  9379,  15246,    284,   7834,  19900,  64663,  97582,  39838,   5801,
          23113,     28,     11,  10034,   3560,  10829,     16,     15,     15,
              8],
        [ 99425, 115641,  99662, 100260, 100658, 121989, 100057, 151643, 151643,
         151643, 151643, 151643, 151643, 151643, 151643, 151643, 151643, 151643,
         151643]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])}
    """


def calculate_ppl_normalize_sentence(
    sentence: str,
    tokenizer: AutoTokenizer,
    model: AutoModelForCausalLM,
    device: torch.device = "cpu",
):
    inputs = tokenizer([sentence], return_tensors="pt")
    with torch.no_grad():
        inputs = inputs.to(device)
        model = model.to(device)
        outputs = model(**inputs)
        loss_list = compute_loss(
            outputs.logits, inputs["input_ids"], inputs["attention_mask"]
        )
        return loss_list.item()


def compute_loss(
    logits: torch.Tensor, labels: torch.Tensor, attn_mask: torch.Tensor = None
):
    """
    logits: t1  t2 t3 ... </s>
    inputs: <s> t1 t2 ... tn
    labels: <s> t1 t2 ... tn
    """
    shift_logits = logits[:, :-1, :].contiguous()
    shift_labels = labels[:, 1:].contiguous()
    shift_attn_mask = attn_mask[:, 1:].contiguous()
    # attention mask where 1 indicates a valid token and 0 an ignored one.
    shift_labels[shift_attn_mask == 0] = -100
    # loss_fn = torch.nn.CrossEntropyLoss(reduction="mean", ignore_index=-100)
    loss_fn = torch.nn.CrossEntropyLoss(reduction="sum", ignore_index=-100)
    losses = loss_fn(
        shift_logits.view(-1, shift_logits.size(-1)),
        shift_labels.view(-1),
    )

    return losses


if __name__ == "__main__":
    pretrained_model_name_or_path = ""
    tokenizer = AutoTokenizer.from_pretrained(
        pretrained_model_name_or_path, trust_remote_codes=True
    )
    model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path)
    sentence = "红藕香残玉簟秋"
    ppl = calculate_ppl_normalize_sentence(
        sentence=sentence, model=model, tokenizer=tokenizer
    )
    print(ppl)
