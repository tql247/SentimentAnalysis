<template>
  <div class="page-content grey lighten-5">
    <v-overlay :value="isLoading">
      <div class="process-bar">
        <v-progress-circular
          :size="50"
          color="amber"
          indeterminate
        ></v-progress-circular>
      </div>
    </v-overlay>

    <div class="app-content d-flex">
      <div class="controller bg-white">
        <div class="select-file thin-border">
          <v-card tile class="lighten-5 file-list" light flat>
            <v-toolbar flat light>
              <v-list-item-avatar>
                <v-icon large color="#F9A825">
                  mdi-file-upload-outline
                </v-icon>
              </v-list-item-avatar>
              <input
                id="mainfilesUpload"
                ref="mainfilesUpload"
                class="input-multi-upload"
                type="file"
                multiple
                name="files"
                accept=".pdf, .docx, .doc, .jpg, .png"
                @change="readMultiFileAsDataURL($event, 'main')"
              />
              <v-toolbar-title class="title">Văn bản đang chọn</v-toolbar-title>
            </v-toolbar>

            <v-list class="list-item">
              <div v-for="(item, index) in items" :key="index" value="true">
                <div class="mainfile d-flex cursor-pointer">
                  <div class="mutil-btn-inline d-flex">
                    <v-btn
                      icon
                      @click="
                        collapseAttach(
                          `iconmdi${index}`,
                          `attachitemid${index}`
                        )
                      "
                    >
                      <v-icon :id="`iconmdi${index}`" class="icon-index active"
                        >mdi-chevron-down</v-icon
                      >
                    </v-btn>
                  </div>
                  <v-list-item-content>
                    <v-list-item-title
                      v-text="item.fileName"
                    ></v-list-item-title>
                  </v-list-item-content>
                  <v-list-item-action>
                    <div class="mutil-btn-inline d-flex">
                      <v-btn icon @click="chooseFileUpload($event, 'attach')">
                        <v-icon color="pink">mdi-attachment</v-icon>
                        <input
                          class="input-multi-upload"
                          type="file"
                          accept=".pdf, .docx, .doc, .jpg, .png"
                          multiple
                          @change="
                            readMultiFileAsDataURL(
                              $event,
                              'attach',
                              item.fileName,
                              `attachitemid${index}`,
                              `iconmdi${index}`
                            )
                          "
                        />
                      </v-btn>
                      <v-btn icon @click="handlePreview(item.fileName)">
                        <v-icon color="info">mdi-eye</v-icon>
                      </v-btn>
                      <v-btn icon @click="removeFile(item.fileName)">
                        <v-icon color="red">mdi-close</v-icon>
                      </v-btn>
                    </div>
                  </v-list-item-action>
                </div>

                <div :id="`attachitemid${index}`" class="list-attach drawer">
                  <v-list-item
                    v-for="attach in item.lsAttach"
                    :key="attach"
                    class="item-attach"
                    @click="1"
                  >
                    <v-list-item-content>
                      <v-list-item-title v-text="attach"></v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-action>
                      <div class="mutil-btn-inline d-flex">
                        <v-btn icon @click="handlePreview(attach)">
                          <v-icon color="info">mdi-eye</v-icon>
                        </v-btn>
                        <v-btn
                          icon
                          @click="removeAttach($event, item.fileName, attach)"
                        >
                          <v-icon color="red">mdi-close</v-icon>
                        </v-btn>
                      </div>
                    </v-list-item-action>
                  </v-list-item>
                </div>
              </div>
            </v-list>

            <div class="mutil-btn-inline d-flex">
              <v-btn
                large
                color="info"
                class="btn"
                light
                tile
                @click="chooseFileUpload($event, 'main')"
              >
                {{ items.length === 0 ? 'Chọn văn bản tải lên' : 'Chọn thêm' }}
                <v-icon size="20" color="white">mdi-plus</v-icon>
              </v-btn>
            </div>
          </v-card>
        </div>
        <div class=" mutil-btn-inline d-flex">
          <v-btn
            v-if="items.length !== 0"
            large
            color="#E53935"
            class="btn"
            dark
            tile
            @click="cancelQueue()"
          >
            Hủy
            <v-icon size="20" color="white">mdi-trash-can-outline</v-icon>
          </v-btn>
          <v-btn
            large
            color="#0277BD"
            class="btn"
            dark
            tile
            @click="uploadFile()"
          >
            Tải lên
            <v-icon size="20" color="#FFFFFF">mdi-arrow-up-bold-circle</v-icon>
          </v-btn>
        </div>
        <div class="thin-border bg-white list-file-uploaded">
          <v-card tile class="lighten-5 file-list" light flat>
            <v-toolbar flat light>
              <v-list-item-avatar>
                <v-icon color="#00C853" large>mdi-text-box-check</v-icon>
              </v-list-item-avatar>
              <v-toolbar-title class="title">Đã tải</v-toolbar-title>
            </v-toolbar>

            <v-list class="list-item">
              <div v-for="(item, index) in items3" :key="index" value="true">
                <div class="d-flex cursor-pointer">
                  <div class="mutil-btn-inline d-flex">
                    <v-btn
                      icon
                      @click="
                        collapseAttach(
                          `iconmdi${index}`,
                          `attachitemuploadedid${index}`
                        )
                      "
                    >
                      <v-icon :id="`iconmdi${index}`" class="icon-index"
                        >mdi-chevron-down</v-icon
                      >
                    </v-btn>
                  </div>
                  <v-list-item-content>
                    <v-list-item-title
                      v-text="item.fileName"
                    ></v-list-item-title>
                  </v-list-item-content>
                  <v-list-item-action>
                    <div class="mutil-btn-inline d-flex">
                      <v-btn icon @click="handlePreview(item.fileName)">
                        <v-icon color="info">mdi-eye</v-icon>
                      </v-btn>
                    </div>
                  </v-list-item-action>
                </div>

                <div
                  :id="`attachitemuploadedid${index}`"
                  class="list-attach drawer"
                >
                  <v-list-item
                    v-for="(attach, index2) in item.attach"
                    :key="index2"
                    @click="1"
                  >
                    <v-list-item-content>
                      <v-list-item-title v-text="attach"></v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-action>
                      <div class="mutil-btn-inline d-flex">
                        <v-btn icon @click="handlePreview(attach)">
                          <v-icon color="info">mdi-eye</v-icon>
                        </v-btn>
                      </div>
                    </v-list-item-action>
                  </v-list-item>
                </div>
              </div>
            </v-list>
          </v-card>
        </div>
      </div>
      <div class="preview bg-white thin-border">
        <div class="doc-preview">
          <v-toolbar flat light>
            <v-list-item-avatar>
              <v-icon color="info" large>mdi-eye</v-icon>
            </v-list-item-avatar>
            <v-toolbar-title class="title">Xem thử</v-toolbar-title>
          </v-toolbar>
          <object
            class="doc-data"
            :data="fileData[previewData]"
            type="application/pdf"
          ></object>
        </div>
      </div>
    </div>
  </div>
</template>

<script src="./index.js"></script>
<style lang="scss" src="./index.scss" scoped></style>
