cd ../
CUDA_VISIBLE_DEVICES=0 python3.7 tools/test.py configs/gfl/gfl_r50_fpn_1x_coco.py ../PaddleDetection/gfl_debug_tools/gfl_r50_fpn_1x_coco_20200629_121244-25944287.pth  --eval bbox
CUDA_VISIBLE_DEVICES=0 python3.7 tools/train.py configs/gfl/gfl_r50_fpn_1x_coco.py

