from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

## SETUP DATA COLLECTION

BoardShim.enable_dev_board_logger()
params = BrainFlowInputParams()
params.ip_port = 6677
params.ip_port_aux = 6678
params.ip_address = "225.1.1.1"
params.ip_address_aux = "225.1.1.1"
params.master_board = BoardIds.SYNTHETIC_BOARD
board = BoardShim(BoardIds.SYNTHETIC_BOARD, params)