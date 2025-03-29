def convert_to_tensorrt(onnx_path, engine_path):
    import tensorrt as trt
    
    TRT_LOGGER = trt.Logger(trt.Logger.WARNING)
    builder = trt.Builder(TRT_LOGGER)
    network = builder.create_network(1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH))
    parser = trt.OnnxParser(network, TRT_LOGGER)
    
    with open(onnx_path, 'rb') as model:
        parser.parse(model.read())
        
    config = builder.create_builder_config()
    config.set_flag(trt.BuilderFlag.FP16)
    serialized_engine = builder.build_serialized_network(network, config)
    
    with open(engine_path, 'wb') as f:
        f.write(serialized_engine)