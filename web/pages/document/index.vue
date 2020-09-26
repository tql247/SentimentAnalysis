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

    <v-row class="fill-height app-content document">
      <v-col cols="12" sm="12" md="12" lg="3" xl="3" class="table-content">
        <div class="table-of-conent">
          <div class="title">Table of content</div>
          <ul>
            <li><a href="#sec1">Tieu de 1</a></li>
            <li><a href="#sec2">Tieu de 2</a></li>
          </ul>
        </div>
      </v-col>
      <v-col
        cols="12"
        sm="12"
        md="12"
        lg="7"
        xl="9"
        class="document-text thin-border"
      >
        <div id="sec1" class="section">Tiêu đề phần 1</div>
        <div class="subsection">Tiêu đề con</div>
        <div>
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Libero
          similique id, dolor et commodi adipisci debitis repudiandae, rerum
          exercitationem harum aliquam possimus dolores officia dolore maiores
          quos hic porro veniam? Lorem ipsum, dolor sit amet consectetur
          adipisicing elit. Libero similique id, dolor et commodi adipisci
          debitis repudiandae, rerum exercitationem harum aliquam possimus
          dolores officia dolore maiores quos hic porro veniam? Lorem ipsum,
          dolor sit amet consectetur adipisicing elit. Libero similique id,
          dolor et commodi adipisci debitis repudiandae, rerum exercitationem
          harum aliquam possimus dolores officia dolore maiores quos hic porro
          veniam? Lorem ipsum, dolor sit amet consectetur adipisicing elit.
          Libero similique id, dolor et commodi adipisci debitis repudiandae,
          rerum exercitationem harum aliquam possimus dolores officia dolore
          maiores quos hic porro veniam? Lorem ipsum, dolor sit amet consectetur
          adipisicing elit. Libero similique id, dolor et commodi adipisci
          debitis repudiandae, rerum exercitationem harum aliquam possimus
          dolores officia dolore maiores quos hic porro veniam? Lorem ipsum,
          dolor sit amet consectetur adipisicing elit. Libero similique id,
          dolor et commodi adipisci debitis repudiandae, rerum exercitationem
          harum aliquam possimus dolores officia dolore maiores quos hic porro
          veniam? Lorem ipsum, dolor sit amet consectetur adipisicing elit.
          Libero similique id, dolor et commodi adipisci debitis repudiandae,
          rerum exercitationem harum aliquam possimus dolores officia dolore
          maiores quos hic porro veniam? Lorem ipsum, dolor sit amet consectetur
          adipisicing elit. Libero similique id, dolor et commodi adipisci
          debitis repudiandae, rerum exercitationem harum aliquam possimus
          dolores officia dolore maiores quos hic porro veniam? Lorem ipsum,
          dolor sit amet consectetur adipisicing elit. Libero similique id,
          dolor et commodi adipisci debitis repudiandae, rerum exercitationem
          harum aliquam possimus dolores officia dolore maiores quos hic porro
          veniam? Lorem ipsum, dolor sit amet consectetur adipisicing elit.
          Libero similique id, dolor et commodi adipisci debitis repudiandae,
          rerum exercitationem harum aliquam possimus dolores officia dolore
          maiores quos hic porro veniam? Lorem ipsum, dolor sit amet consectetur
          adipisicing elit. Libero similique id, dolor et commodi adipisci
          debitis repudiandae, rerum exercitationem harum aliquam possimus
          dolores officia dolore maiores quos hic porro veniam? Lorem ipsum,
          dolor sit amet consectetur adipisicing elit. Libero similique id,
          dolor et commodi adipisci debitis repudiandae, rerum exercitationem

          <div v-katex:auto class="formular">
            \(\frac{a_i}{1+x}\)
          </div>

          <div class="content-img">
            <img class="img" src="/bg.png" />
            <div class="label">Mô tả hình ảnh</div>
            <div class="ref">Nguồn <a href="#">abc</a></div>
          </div>

          harum aliquam possimus dolores officia dolore maiores quos hic porro
          veniam? Lorem ipsum, dolor sit amet consectetur adipisicing elit.
          Libero similique id, dolor et commodi adipisci debitis repudiandae,
          rerum exercitationem harum aliquam possimus dolores officia dolore
          maiores quos hic porro veniam? Lorem ipsum, dolor sit amet consectetur
          adipisicing elit. Libero similique id, dolor et commodi adipisci
          debitis repudiandae, rerum exercitationem harum aliquam possimus
          dolores officia dolore maiores quos hic porro veniam? Lorem ipsum,
          dolor sit amet consectetur adipisicing elit. Libero similique id,
          dolor et commodi adipisci debitis repudiandae, rerum exercitationem
          harum aliquam possimus dolores officia dolore maiores quos hic porro
          veniam? Lorem ipsum, dolor sit amet consectetur adipisicing elit.
          Libero similique id, dolor et commodi adipisci debitis repudiandae,
          rerum exercitationem harum aliquam possimus dolores officia dolore
          maiores quos hic porro veniam? Lorem ipsum, dolor sit amet consectetur
          adipisicing elit. Libero similique id, dolor et commodi adipisci
          debitis repudiandae, rerum exercitationem harum aliquam possimus
          dolores officia dolore maiores quos hic porro veniam? Lorem ipsum,
          dolor sit amet consectetur adipisicing elit. Libero similique id,
          dolor et commodi adipisci debitis repudiandae, rerum exercitationem
          harum aliquam possimus dolores officia dolore maiores quos hic porro
          veniam?

          <div id="sec2" class="section">Tiêu đề phần 2</div>
          <div class="subsection">Tiêu đề con</div>
        </div>
      </v-col>
    </v-row>
  </div>
</template>
<script src="./index.js"></script>
<style lang="scss" src="./index.scss" scoped></style>
