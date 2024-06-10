SAMPLERS = [
    "euler",
    "euler_ancestral",
    "heun",
    "heunpp2",
    "dpm_2",
    "dpm_2_ancestral",
    "lms",
    "dpm_fast",
    "dpm_adaptive",
    "dpmpp_2s_ancestral",
    "dpmpp_sde",
    "dpmpp_sde_gpu",
    "dpmpp_2m",
    "dpmpp_2m_sde",
    "dpmpp_2m_sde_gpu",
    "dpmpp_3m_sde",
    "dpmpp_3m_sde_gpu",
    "ddpm",
    "lcm",
    "ddim",
    "uni_pc",
    "uni_pc_bh2",
]

SCHEDULERS = [
    "normal",
    "karras",
    "exponential",
    "sgm_uniform",
    "simple",
    "ddim_uniform",
]

CONTROLNET_PREPROCESSORS = [
    # Common
    "CannyEdgePreprocessor",
    "AnyLineArtPreprocessor_aux",
    "LineArtPreprocessor",
    "LineartStandardPreprocessor",
    "MiDaS-DepthMapPreprocessor",
    "DepthAnythingPreprocessor",
    "Zoe-DepthMapPreprocessor",
    "Zoe_DepthAnythingPreprocessor",
    "HEDPreprocessor",
    "OpenposePreprocessor",
    "DWPreprocessor",

    # Less common
    "AnimalPosePreprocessor",
    "AnimeFace_SemSegPreprocessor",
    "AnimeLineArtPreprocessor",
    "BAE-NormalMapPreprocessor",
    "BinaryPreprocessor",
    "ColorPreprocessor",
    "DSINE-NormalMapPreprocessor",
    "DensePosePreprocessor",
    "DiffusionEdge_Preprocessor",
    "FakeScribblePreprocessor",
    "ImageIntensityDetector",
    "ImageLuminanceDetector",
    "LeReS-DepthMapPreprocessor",
    "M-LSDPreprocessor",
    "Manga2Anime_LineArt_Preprocessor",
    "MediaPipe-FaceMeshPreprocessor",
    "MeshGraphormer-DepthMapPreprocessor",
    "Metric3D-DepthMapPreprocessor",
    "Metric3D-NormalMapPreprocessor",
    "MiDaS-NormalMapPreprocessor",
    "OneFormer-ADE20K-SemSegPreprocessor",
    "OneFormer-COCO-SemSegPreprocessor",
    "PiDiNetPreprocessor",
    "SAMPreprocessor",
    "ScribblePreprocessor",
    "Scribble_PiDiNet_Preprocessor",
    "Scribble_XDoG_Preprocessor",
    "SemSegPreprocessor",
    "ShufflePreprocessor",
    "TEEDPreprocessor",
    "TTPlanet_TileGF_Preprocessor",
    "TTPlanet_TileSimple_Preprocessor",
    "TilePreprocessor",
    "UniFormer-SemSegPreprocessor",
]

CONTROLNET_MODELS = [
    "control_boxdepth_LooseControlfp16.safetensors",
    "control_sd15_inpaint_depth_hand_fp16.safetensors",
    "control_v11e_sd15_ip2p.pth",
    "control_v11e_sd15_shuffle.pth",
    "control_v11f1e_sd15_tile.pth",
    "control_v11f1p_sd15_depth.pth",
    "control_v11p_sd15_canny.pth",
    "control_v11p_sd15_lineart.pth",
    "control_v11p_sd15_mlsd.pth",
    "control_v11p_sd15_normalbae.pth",
    "control_v11p_sd15_openpose.pth",
    "control_v11p_sd15_scribble.pth",
    "control_v11p_sd15_seg.pth",
    "control_v11p_sd15_softedge.pth",
    "control_v11p_sd15s2_lineart_anime.pth",
    "control_v11u_sd15_tile_fp16.safetensors",
    "control_v1p_sd15_qrcode_monster.safetensors",
    "control_v1p_sdxl_qrcode_monster.safetensors",
    "controlnet-canny-sdxl-1.0.safetensors",
    "controlnet-canny-sdxl-1.0_V2.safetensors",
    "controlnet-depth-sdxl-1.0.fp16.safetensors",
    "controlnet-openpose-sdxl-1.0.safetensors",
    "controlnet-openpose-sdxl-1.0_twins.safetensors",
    "controlnet-scribble-sdxl-1.0.safetensors",
    "controlnet-sd-xl-1.0-softedge-dexined.safetensors",
    "depth-anything.safetensors",
    "depth-zoe-xl-v1.0-controlnet.safetensors",
    "diffusers_xl_canny_full.safetensors",
    "diffusers_xl_canny_mid.safetensors",
    "diffusers_xl_canny_small.safetensors",
    "diffusers_xl_depth_full.safetensors",
    "diffusers_xl_depth_mid.safetensors",
    "diffusers_xl_depth_small.safetensors",
    "ioclab_sd15_recolor.safetensors",
    "mistoLine_fp16.safetensors",
    "mistoLine_rank256.safetensors",
    "OpenPoseXL2.safetensors",
    "sargezt_xl_depth.safetensors",
    "sargezt_xl_depth_faid_vidit.safetensors",
    "sargezt_xl_depth_zeed.safetensors",
    "sargezt_xl_softedge.safetensors",
    "t2i-adapter_diffusers_xl_canny.safetensors",
    "t2i-adapter_diffusers_xl_depth_midas.safetensors",
    "t2i-adapter_diffusers_xl_depth_zoe.safetensors",
    "t2i-adapter_diffusers_xl_lineart.safetensors",
    "t2i-adapter_diffusers_xl_openpose.safetensors",
    "t2i-adapter_diffusers_xl_sketch.safetensors",
    "t2i-adapter_xl_canny.safetensors",
    "t2i-adapter_xl_openpose.safetensors",
    "t2i-adapter_xl_sketch.safetensors",
    "t2iadapter_canny_sd14v1.pth",
    "t2iadapter_color_sd14v1.pth",
    "t2iadapter_depth_sd14v1.pth",
    "t2iadapter_keypose_sd14v1.pth",
    "t2iadapter_openpose_sd14v1.pth",
    "t2iadapter_seg_sd14v1.pth",
    "t2iadapter_sketch_sd14v1.pth",
    "t2iadapter_style_sd14v1.pth",
    "thibaud_xl_openpose.safetensors",
    "thibaud_xl_openpose_256lora.safetensors"

    # Lora
    "control-lora-canny-rank128.safetensors",
    "control-lora-canny-rank256.safetensors",
    "control-lora-depth-rank128.safetensors",
    "control-lora-depth-rank256.safetensors",
    "control-lora-recolor-rank128.safetensors",
    "control-lora-recolor-rank256.safetensors",
    "control-lora-sketch-rank128-metadata.safetensors",
    "control-lora-sketch-rank256.safetensors",
    "control_lora_rank128_v11e_sd15_ip2p_fp16.safetensors",
    "control_lora_rank128_v11e_sd15_shuffle_fp16.safetensors",
    "control_lora_rank128_v11f1e_sd15_tile_fp16.safetensors",
    "control_lora_rank128_v11f1p_sd15_depth_fp16.safetensors",
    "control_lora_rank128_v11p_sd15_canny_fp16.safetensors",
    "control_lora_rank128_v11p_sd15_inpaint_fp16.safetensors",
    "control_lora_rank128_v11p_sd15_lineart_fp16.safetensors",
    "control_lora_rank128_v11p_sd15_mlsd_fp16.safetensors",
    "control_lora_rank128_v11p_sd15_normalbae_fp16.safetensors",
    "control_lora_rank128_v11p_sd15_openpose_fp16.safetensors",
    "control_lora_rank128_v11p_sd15_scribble_fp16.safetensors",
    "control_lora_rank128_v11p_sd15_seg_fp16.safetensors",
    "control_lora_rank128_v11p_sd15_softedge_fp16.safetensors",
    "control_lora_rank128_v11p_sd15s2_lineart_anime_fp16.safetensors",
    "sai_xl_canny_128lora.safetensors",
    "sai_xl_canny_256lora.safetensors",
    "sai_xl_depth_128lora.safetensors",
    "sai_xl_depth_256lora.safetensors",
    "sai_xl_recolor_128lora.safetensors",
    "sai_xl_recolor_256lora.safetensors",
    "sai_xl_sketch_128lora.safetensors",
    "sai_xl_sketch_256lora.safetensors",
]
