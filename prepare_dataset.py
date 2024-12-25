import os
import shutil
import argparse
import torch

def merge_datasets(root_folder, output_folder):
    # Tạo hai thư mục 0_real và 1_fake trong output_folder
    os.makedirs(os.path.join(output_folder, "0_real"), exist_ok=True)
    os.makedirs(os.path.join(output_folder, "1_fake"), exist_ok=True)

    # Duyệt qua tất cả các thư mục con trong root_folder
    for sub_folder in os.listdir(root_folder):
        sub_folder_path = os.path.join(root_folder, sub_folder)

        # Kiểm tra nếu là thư mục
        if os.path.isdir(sub_folder_path):
            # Duyệt qua từng class (0_real và 1_fake)
            for class_name in ["0_real", "1_fake"]:
                class_path = os.path.join(sub_folder_path, class_name)
                if os.path.exists(class_path):
                    # Duyệt qua từng file trong class folder
                    for file_name in os.listdir(class_path):
                        file_path = os.path.join(class_path, file_name)
                        # Đường dẫn đích
                        dest_path = os.path.join(output_folder, class_name, file_name)
                        
                        # Tránh ghi đè file trùng tên
                        if os.path.exists(dest_path):
                            base_name, ext = os.path.splitext(file_name)
                            counter = 1
                            while os.path.exists(dest_path):
                                file_name = f"{base_name}_{counter}{ext}"
                                dest_path = os.path.join(output_folder, class_name, file_name)
                                counter += 1
                        
                        # Di chuyển file
                        shutil.move(file_path, dest_path)

    print("Hoàn thành việc gộp dữ liệu.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gộp dataset từ các thư mục con thành một thư mục chung.")
    parser.add_argument("--root_folder", type=str, required=True, help="Thư mục gốc chứa các folder con.")
    parser.add_argument("--output_folder", type=str, required=True, help="Thư mục đích để gộp dữ liệu.")

    args = parser.parse_args()
    merge_datasets(args.root_folder, args.output_folder)


# import torch.nn as nn


# chk = torch.load(r"D:\K32\do_an_tot_nghiep\ADOF\weights\dino_deitsmall16_pretrain_full_checkpoint.pth")
# chk2 = torch.load(r"D:\K32\do_an_tot_nghiep\ADOF\weights\dino_deitsmall16_pretrain_full_checkpoint.pth")
# model = torch.hub.load('facebookresearch/dino:main', 'dino_vits16')

# import vision_transformer as vits
# from vision_transformer import DINOHead
# import utils
# vit = vits.__dict__['vit_small_from_checkpoint']()


# embed_dim = vit.embed_dim
# out_dim = 65536
# use_bn_in_head = False
# norm_last_layer = False

# student = utils.MultiCropWrapper(vit, DINOHead(
#     embed_dim,
#     out_dim,
#     use_bn=use_bn_in_head,
#     norm_last_layer=norm_last_layer,
# ))

# student.to(device)
# student = nn.parallel.DistributedDataParallel(student,None)

# # Xóa 'module.' khỏi các key trong state_dict
# state_dict = chk2['student']
# new_state_dict = {}
# for key, value in state_dict.items():
#     new_key = key.replace('module.', '')  # Xóa tiền tố 'module.'
#     new_state_dict[new_key] = value


# device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')


# student.load_state_dict(new_state_dict)



















