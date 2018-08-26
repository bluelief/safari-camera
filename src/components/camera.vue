// Copyright (c) 2018 Bluelief.
// Licensed under the MIT License.

<template>
  <div id="app">
    {{ text }}
    <br />
    <br />
    <div><video ref="video" id="video" width="640" height="480" autoplay playsinline></video></div>
    <br />
    <br />
    <div><button id="snap" v-on:click="capture()">Snap Photo</button></div>
    <br />
    <br />
    <canvas ref="canvas" id="canvas" width="640" height="480"></canvas>
  </div>
</template>

<script>
const axios = require('axios')

export default {
  name: 'app',
  data () {
    return {
      video: {},
      canvas: null,
      captures: null,
      text: 'debug text',
      url: 'https://localhost/barcode/',
    }
  },
  mounted () {
    const medias = {
      audio: false,
      video: {
        facingMode: {
          exact: 'environment'
        }
      }
    }
    this.video = this.$refs.video
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia(medias)
        .then(stream => (this.video.srcObject = stream))
        .catch(err => (console.log(err)))
    }
  },
  methods: {
    capture () {
      this.canvas = this.$refs.canvas
      var context = this.canvas.getContext("2d").drawImage(this.video, 0, 0, 640, 480)
      this.captures = canvas.toDataURL("image/jpeg")
    }
  },
  watch: {
    captures: {
      handler: function () {
        let params = new URLSearchParams()
        params.append('image', this.captures.replace(/^.*,/, ''))

        axios
          .post(this.url, params)
          .then(response => (this.text = response.data))
          .catch(response => (this.text = 'error'))
      }
    }
  }
}
</script>

<style>
body {
  background-color: #000000;
}

#app {
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#video {
  background-color: #000000;
  display: block;
}

#canvas {
  display: none;
}
</style>
