gci_unet_train 3d_fullres gci_unet_trainer_lung 6 1&&
gci_unet_predict -i /srv/qiaoqiang/DATASET/gci_unet_raw/gci_unet_raw_data/Task006_Lung/imagesTs -o ~/GCI-UNet/gciunet/evaluation/gci_unet_lung_checkpoint/inferTs1 -m 3d_fullres  -t 6 -f 1 -chk model_best -tr gci_unet_trainer_lung