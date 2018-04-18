<template>
    <ul class="timeline">
        <li class="time-label">
                  <span class="bg-red">
                   {{ video.published | date }}
                  </span>
        </li>

        <li>
            <i class="fa fa-video-camera bg-blue"></i>

            <div class="timeline-item">
                <h3 class="timeline-header">
                    <a href="javascript:void(0)">{{ video.uploader }}</a> uploaded a video:
                </h3>

                <div class="timeline-body">
                    <div class="embed-responsive embed-responsive-16by9">
                        <iframe class="embed-responsive-item" :src="'https://www.youtube.com/embed/' + video.id"
                                frameborder="0" allowfullscreen=""></iframe>
                    </div>
                </div>
            </div>
        </li>

        <li v-for="comment in video.comments">
            <i :class="'fa fa-comments ' + getSentimentColor(comment.sentiments)"></i>

            <div class="timeline-item">
                <h3 class="timeline-header"><a href="javascript:void(0)">{{ comment.author }}</a> commented:</h3>

                <div class="timeline-body">
                    {{ comment.text }}
                </div>
                <div class="timeline-footer">
                    <a style="margin-right: 5px;" :class="'btn btn-flat btn-xs ' + getConfidenceColor(sentiment)" v-for="sentiment in comment.sentiments">
                        <i :class="getIcon(sentiment)"></i>
                        {{ sentiment.confidence*100 }} %
                    </a>
                </div>
            </div>
        </li>

        <li>
            <i class="fa fa-clock-o bg-gray"></i>
        </li>
    </ul>
</template>

<script>
    export default {

        name: 'VideoDetails',

        props: ['video'],

        data() {
            return {}
        },

        methods: {
            getSentimentColor(sentiments) {
                switch (sentiments[0].sentiment){
                    case 'positive':
                        return 'bg-green';
                    case 'negative':
                        return 'bg-red';
                    case 'neutral':
                        return 'bg-gray';
                }
            },

            getConfidenceColor(sentiment) {
                switch (sentiment.sentiment){
                    case 'positive':
                        return 'btn-success';
                    case 'negative':
                        return 'btn-danger';
                    case 'neutral':
                        return 'btn-default';
                }
            },

            getIcon(sentiment) {
                switch (sentiment.sentiment){
                    case 'positive':
                        return 'fa fa-thumbs-up';
                    case 'negative':
                        return 'fa fa-thumbs-down';
                    case 'neutral':
                        return 'fa fa-circle-o';
                }
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