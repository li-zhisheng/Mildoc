# MilDoc 企业知识库系统

## 项目简介



**Mildoc** 是一款面向企业的智能知识库管理平台，专注于将企业分散的文档资产转化为可检索、可交互的智能知识中心。通过集成 MinIO 对象存储、Milvus 向量数据库及大语言模型，Mildoc 提供从文档上传、自动解析、向量化存储到智能问答的全流程解决方案，帮助企业构建统一、高效、安全的知识管理底座。



![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NWJiZGIxYzhmZDZlZTcwY2U1MzMxMWZiNmYxNjJkZTBfNjk0NDc2YTM4YjA4MDkzOTA0OTA3MTA4ZDNhOTNmYmFfSUQ6NzY0NTExNzY0NTI1MTMzMzA3Nl8xNzgyNjg2MjI4OjE3ODI3NzI2MjhfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTVjN2EyZTkyZDBkZmRiY2ZmOTVkNDMwYThlZDczZWZfNTA4MzllNDEyMTAwZGRhMTc0NjU5NTI1MjhmZWU1YzdfSUQ6NzY0NTExNzY0MzM0NzMzMjAzOV8xNzgyNjg2MjI4OjE3ODI3NzI2MjhfVjM)



![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZmFiYzVhMTE1MjJhNzM2MmQ5NjA4ODIxZTY5MWYwMzBfN2NkZDRmMjA0NmVmOTk2MDQ2YTc3YWU3MDY5ZDc1MjRfSUQ6NzY0NTExNzY0NDE4MjAxNDkyOF8xNzgyNjg2MjI4OjE3ODI3NzI2MjhfVjM)



## 系统概述



本系统基于 MinIO 对象存储和 Milvus 向量数据库，构建了一套完整的企业知识管理解决方案。

系统包含三个核心模块：

文档索引服务（mildoc\_index）

管理系统（mildoc\_admin）

微信客服接口（mildoc\_wxkf）





![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTU4YTdiNjFkNWM1NjQzMjFjOWEwMTg1YmRkYmE3NTNfZGY5MzQxNWFmYTkxYWFmM2Q4Nzg5NTI4NmRjMTFjZDdfSUQ6NzY0NTExNzY0NDg2NTU1NTM5OV8xNzgyNjg2MjI4OjE3ODI3NzI2MjhfVjM)





## 业务系统

### mildoc\_admin（文档管理系统）

- 创建/删除目录结构

- 添加/删除文档对象

- 查看文档元信息（文件名、MD5、创建时间）

- 查看文档向量化状态和切片信息



### mildoc\_index（文档索引服务）

- 监听 MinIO 指定桶的对象事件

- 调用文档解析器进行文档解析和分片

- 生成文档向量并存储到 Milvus

- 处理文档删除时的向量清理



### mildoc\_wxkf（微信客服接口）

- 接收微信客服转发的用户咨询

- 使用 LangChain 进行智能检索

- 调用 LLM 生成智能解答

- 返回答案给微信客服系统



## 技术实现

### 文档解析器

- **PDF解析器**：处理 PDF 文档

- **Office解析器**：处理 Word、Excel、PowerPoint 文档

- **MinerU解析器**：高精度文档解析

- **Markdown解析器**：处理 Markdown 文档

- **Text解析器**：处理纯文本文档

### Embedding

- 将文本分片转换为向量表示

- 支持多种向量模型

### LangChain

- **Retrieve**：基于向量相似度的文档检索

- **Rerank**：对检索结果进行重新排序优化

### LLM服务

- 基于检索到的文档上下文生成智能解答

- 支持多种大语言模型



## 技术特点



### 事件驱动架构

- 基于 MinIO 对象事件的自动化文档处理

- 实时响应文档的创建和删除操作

- 确保存储和向量数据的一致性

### 多格式文档支持

- 支持 PDF、Word、Excel、PowerPoint、Markdown、Text 等格式

- 内置多种专业解析器，包括高精度的 MinerU 解析器

- 统一的文本分片和向量化处理流程

### 智能检索问答

- 基于向量相似度的语义搜索

- LangChain 框架实现 Retrieve \+ Rerank 优化

- LLM 驱动的上下文感知智能解答





## 数据流转说明



1. **文档上传流程**：用户上传文档 → MinIO 存储 → 触发事件 → 文档解析 → 向量生成 → 存储到 Milvus

2. **智能问答流程**：用户咨询 → 微信客服 → 向量检索 → 文档匹配 → LLM 分析 → 智能回答

3. **文档管理流程**：管理员操作 → 查询元信息 → 展示文档状态和切片信息

4. **数据同步流程**：文档删除 → MinIO 清理 → 事件触发 → Milvus 向量清理



