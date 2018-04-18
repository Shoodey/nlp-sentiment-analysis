<template>
    <div class="box box-info">
        <div class="box-header with-border">
            <h3 class="box-title">{{ category }} videos ({{ videos.videos.length }})</h3>

            <div class="box-tools pull-right">
                <button type="button" class="btn btn-box-tool" data-widget="collapse">
                    <i class="fa fa-minus"></i>
                </button>
            </div>
        </div>

        <div class="box-body" style="">
            <div class="table-responsive">
                <table class="table no-margin">
                    <thead>
                    <tr>
                        <th>Video</th>
                        <th>Title</th>
                        <th>Duration</th>
                        <th>Views</th>
                        <th>Comments</th>
                        <th>Published on</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="video in videos.videos">
                        <td><a :href="'https://www.youtube.com/watch?v=' + video.id" target="_blank">
                            <img style="max-width: 80px" :src="'https://img.youtube.com/vi/' + video.id + '/0.jpg'"
                                 alt="">
                        </a></td>
                        <td style="line-height: 60px">
                            <a href="javascript:void(0)" @click="setVideo(video)">
                                {{ video.title }}
                            </a>
                        </td>
                        <td style="line-height: 60px">{{ video.duration | duration }}</td>
                        <td style="line-height: 60px">{{ video.view_count | bigNumber }}</td>
                        <td style="line-height: 60px">{{ video.comments.length }}</td>
                        <td style="line-height: 60px">{{ video.published | date }}</td>
                    </tr>
                    </tbody>
                </table>
            </div>

        </div>
    </div>
</template>

<script>
    export default {

        name: 'VideosList',

        props: ['category', 'videos', 'video'],

        data() {
            return {}
        },

        methods: {
            setVideo(video) {
                this.$emit('setVideo', video)
            }
        },

        filters: {
            duration(value) {
                return numeral(value).format('00:00:00')
            },

            bigNumber(value) {
                return numeral(value).format('0.0a')
            },

            date(value) {
                return moment.unix(value).format("MMMM Do YYYY");
            }
        }
    }
</script>