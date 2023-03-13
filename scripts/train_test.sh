#!/bin/sh 
 python train.py --deterministic --epochs 5 --optimizer Adam --lr 0.001 --wd 0 --compress policies/schedule-cifar-nas.yaml --model ai85nascifarnet --dataset CIFAR10 --device MAX78000 --batch-size 100 --print-freq 100 --validation-split 0 --use-bias --qat-policy policies/qat_policy_late_cifar.yaml --confusion "$@" 
#!/bin/sh 
 python train.py --epochs 5 --optimizer Adam --lr 0.00032 --wd 0 --compress policies/schedule-cifar100.yaml --model ai85simplenet --dataset CIFAR100 --device MAX78000 --batch-size 32 --print-freq 100 --validation-split 0 --qat-policy None --use-bias "$@" 
#!/bin/sh 
 python train.py --deterministic --epochs 5 --optimizer Adam --lr 0.001 --wd 0 --compress policies/schedule-cifar-nas.yaml --model ai85nascifarnet --dataset CIFAR100 --device MAX78000 --batch-size 100 --print-freq 100 --validation-split 0 --use-bias --qat-policy policies/qat_policy_late_cifar.yaml "$@" 
#!/bin/sh 
 python train.py --deterministic --epochs 5 --optimizer Adam --lr 0.001 --wd 0 --compress policies/schedule-cifar100-effnet2.yaml --model ai87effnetv2 --dataset CIFAR100 --device MAX78002 --batch-size 100 --print-freq 100 --validation-split 0 --use-bias --qat-policy policies/qat_policy_late_cifar.yaml "$@" 
#!/bin/sh 
 python train.py --deterministic --epochs 5 --optimizer SGD --lr 0.1 --compress policies/schedule-cifar100-mobilenetv2.yaml --model ai87netmobilenetv2cifar100_m0_5 --dataset CIFAR100 --device MAX78002 --batch-size 128 --print-freq 100 --validation-split 0 --use-bias --qat-policy policies/qat_policy_cifar100_mobilenetv2.yaml "$@" 
#!/bin/sh 
 python train.py --deterministic --epochs 5 --optimizer SGD --lr 0.1 --compress policies/schedule-cifar100-mobilenetv2.yaml --model ai87netmobilenetv2cifar100_m0_75 --dataset CIFAR100 --device MAX78002 --batch-size 128 --print-freq 100 --validation-split 0 --use-bias --qat-policy policies/qat_policy_cifar100_mobilenetv2.yaml "$@" 
#!/bin/sh 
 python train.py --epochs 5 --optimizer Adam --lr 0.001 --wd 0 --compress policies/schedule-cifar100.yaml --model ai85simplenet --dataset CIFAR100 --device MAX78000 --batch-size 100 --print-freq 250 --validation-split 0 --qat-policy policies/qat_policy_cifar100.yaml --use-bias "$@" 
#!/bin/sh 
 python train.py --epochs 5 --deterministic --optimizer Adam --lr 0.00064 --wd 0 --compress policies/schedule-cifar100-ressimplenet.yaml --model ai85ressimplenet --dataset CIFAR100 --device MAX78000 --batch-size 32 --print-freq 100 --validation-split 0 "$@" 
#!/bin/sh 
 python train.py --epochs 5 --optimizer Adam --lr 0.001 --wd 0 --compress policies/schedule-cifar100.yaml --model ai85simplenetwide2x --dataset CIFAR100 --device MAX78000 --batch-size 100 --print-freq 100 --validation-split 0 --qat-policy policies/qat_policy_cifar100.yaml --use-bias "$@" 
#!/bin/sh 
 python train.py --optimizer SGD --epochs 5 --deterministic --compress policies/schedule.yaml --model ai85net6 --dataset CIFAR10 --confusion --device MAX78000 --lr 0.01 --param-hist "$@" 
#!/bin/sh 
 python train.py --optimizer SGD --epochs 5 --lr 0.02 --compress policies/schedule_squeezenet_cifar10.yaml --model ai85squeezenet --dataset CIFAR10 --confusion --param-hist --device MAX78000 "$@" 
#!/bin/sh 
 python train.py --epochs 5 --optimizer Adam --lr 0.001 --wd 0 --deterministic --compress policies/schedule_kws20.yaml --model ai85kws20net --dataset KWS_20 --confusion --device MAX78000 "$@" 
#!/bin/sh 
 python train.py --epochs 5 --optimizer Adam --lr 0.0006 --wd 0 --deterministic --compress policies/schedule_kws20_v2.yaml --model ai85kws20netv2 --dataset KWS_20 --confusion --device MAX78000 "$@" 
#!/bin/sh 
 python train.py --epochs 5 --optimizer Adam --lr 0.001 --wd 0 --deterministic --compress policies/schedule_kws20.yaml --model ai85kws20netv3 --dataset KWS_20 --confusion --device MAX78000 "$@" 
#!/bin/sh 
 python train.py --lr 0.1 --optimizer SGD --epochs 5 --deterministic --compress policies/schedule.yaml --model ai85net5 --dataset MNIST --confusion --param-hist --pr-curves --embedding --device MAX78000 "$@" 
#!/bin/sh 
 python train.py --lr 0.1 --optimizer SGD --epochs 5 --deterministic --compress policies/schedule.yaml --model ai85netextrasmall --dataset MNIST --confusion --param-hist --pr-curves --embedding --device MAX78000 "$@" 
#!/bin/sh 
 python train.py --lr 0.1 --optimizer SGD --epochs 5 --deterministic --seed 1 --compress policies/schedule.yaml --model ai85net5 --dataset MNIST --confusion --param-hist --pr-curves --embedding --device MAX78000 --qat-policy policies/qat_policy_mnist.yaml "$@" 
