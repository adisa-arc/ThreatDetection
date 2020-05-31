LIB_PREFIX := lib
LIB_EXT := .a
CXX := g++
CC := gcc
AR := ar
RM := rm
CP := cp
MKDIR := mkdir
INSTALL_SCRIPT := install.sh
UNINSTALL_SCRIPT := uninstall.sh
PCAPPLUSPLUS_HOME := /Users/ajcblyth/Projects/IPJSONRPC
# includes
PCAPPP_INCLUDES := 
# libs dir
PCAPPP_LIBS_DIR := 
# libs
PCAPPP_LIBS := -lPcap++ -lPacket++ -lCommon++
# post build
PCAPPP_POST_BUILD :=
# build flags
PCAPPP_BUILD_FLAGS := -I/usr/local/inlcude/pcap
# includes
PCAPPP_INCLUDES += -I/usr/include/netinet
# libs
PCAPPP_LIBS += -lpcap -lpthread -framework SystemConfiguration -framework CoreFoundation
SOURCES := $(wildcard *.cpp)
OBJS_FILENAMES := $(patsubst %.cpp,Obj/%.o,$(SOURCES))
Obj/%.o: %.cpp
	@echo 'Building file: $<'
	$(CXX) $(PCAPPP_BUILD_FLAGS) $(PCAPPP_INCLUDES) -O0 -g -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:Obj/%.o=Obj/%.d)" -MT"$(@:Obj/%.o=Obj/%.d)" -o "$@" "$<"
UNAME := $(shell uname)
CUR_TARGET := $(notdir $(shell pwd))
all: ip2json
start:
	@echo '==> Building target: $(CUR_TARGET)'
create-directories:
	@$(MKDIR) -p Obj
	@$(MKDIR) -p Bin
ip2json: start create-directories $(OBJS_FILENAMES)
	$(CXX) $(PCAPPP_BUILD_FLAGS) $(PCAPPP_LIBS_DIR) -o "./Bin/ipjson$(BIN_EXT)" $(OBJS_FILENAMES) $(PCAPPP_LIBS)
	@echo 'Finished successfully building: $(CUR_TARGET)'
	@echo ' '
clean:
	@$(RM) -rf ./Obj/*
	@$(RM) -rf ./Bin/*
	@echo 'Clean finished: $(CUR_TARGET)'
