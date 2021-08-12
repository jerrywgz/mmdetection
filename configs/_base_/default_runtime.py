checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=1,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = '../PaddleDetection/gfl_debug_tools/gfl_r50_fpn_1x_coco_20200629_121244-25944287.pth' #None
resume_from = None
workflow = [('train', 1)]
