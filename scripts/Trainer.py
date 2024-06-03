from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import is_bfloat16_supported

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = finetuning_dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,#reduce for memory alloc
    dataset_num_proc = 2,#2 or 1,
    packing = False, # Can make training 5x faster for short sequences.
    args = TrainingArguments(
        per_device_train_batch_size = 2, #2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        num_train_epochs = 6, #6, #8
        # max_steps = 60,
        learning_rate = 2e-4,
        fp16 = not torch.cuda.is_bf16_supported(),
        bf16 = torch.cuda.is_bf16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "",
        # gradient_checkpointing=True,  # Enable if supported by the model

    ),
)
trainer_stats = trainer.train()
