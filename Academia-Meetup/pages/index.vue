<template>
  <div>
    <top-bar/>
    <hero/>
    <about/>
    <schedule/>
    <speakers/>
    <sponsor/>
    <hackathon/>
    <register-form/>
    <bottom/>
  </div>
</template>

<script>
  import TopBar from '~/components/TopBar.vue'
  import Hero from '~/components/Hero.vue'
  import About from '~/components/About.vue'
  import Speakers from '~/components/Speakers.vue'
  import Schedule from '~/components/Schedule.vue'
  import Gallery from '~/components/Gallery.vue'
  import Hackathon from '~/components/Hackathon.vue'
  import Sponsor from '~/components/Sponsor.vue'
  import Bottom from '~/components/Bottom.vue'
  import RegisterForm from '~/components/Form.vue'

  export default {
    components: {
      TopBar,
      Hero,
      About,
      Speakers,
      Schedule,
      Gallery,
      Hackathon,
      Sponsor,
      Bottom,
      RegisterForm
    }
  }
</script>