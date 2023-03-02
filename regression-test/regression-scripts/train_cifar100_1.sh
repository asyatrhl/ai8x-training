#!/bin/sh
python train.py --epochs 60 --optimizer Adam --lr 0.00032 --wd 0 --compress regression-policies/schedule-cifar100-v1.yaml --model ai85simplenet --dataset CIFAR100 --device MAX78000 --batch-size 32 --print-freq 100 --validation-split 0 --qat-policy None --use-bias --enable-tensorboard "$@"
