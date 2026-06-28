# 导入MinerU相关模块
from mineru.cli.common import convert_pdf_bytes_to_bytes_by_pypdfium2, prepare_env
from mineru.data.data_reader_writer import FileBasedDataWriter
from mineru.backend.vlm.vlm_analyze import doc_analyze
from mineru.backend.vlm.vlm_middle_json_mkcontent import union_make as vlm_union_make
from mineru.utils.enum_class import MakeMode
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

file_name = "test.pdf"

def parse(data: bytes) -> str:
    """解析PDF文档"""
    try:
        logger.info("正在使用MinerU解析PDF文档...")
        
        # 转换PDF字节数据
        logger.info("正在转换PDF字节数据...")
        pdf_bytes = convert_pdf_bytes_to_bytes_by_pypdfium2(data, 0, None)
        
        local_image_dir, local_md_dir = prepare_env("output1", file_name, "vlm")
        image_writer, md_writer = FileBasedDataWriter(local_image_dir), FileBasedDataWriter(local_md_dir)

        # 使用VLM分析PDF
        logger.info("正在分析PDF文档...")
        middle_json, infer_result = doc_analyze(
            pdf_bytes, 
            backend="http-client", 
            server_url="http://localhost:6006", 
            image_writer=image_writer
        )
        
        # 获取PDF信息
        pdf_info = middle_json["pdf_info"]
        
        # 生成Markdown内容
        logger.info("正在生成Markdown内容...")
        logger.info(local_image_dir)
        md_content_str = vlm_union_make(pdf_info, MakeMode.MM_MD, "https://your.com/" + local_image_dir)
        
        logger.info(f"MinerU解析完成，生成了{len(md_content_str)}字符的Markdown内容")
        return md_content_str.strip()
        
    except ImportError as e:
        logger.error(f"MinerU模块导入失败: {e}")
        logger.error("请确保已正确安装MinerU相关依赖")
        return ""
    except Exception as e:
        logger.error(f"MinerU解析失败: {e}")
        return ""

if __name__ == "__main__":
    with open(file_name, "rb") as f:
        data = f.read()
    result = parse(data)

    with open(file_name + ".with.img.md", "w") as f:
        f.write(result)

    print("-"*100)
    # print(result)