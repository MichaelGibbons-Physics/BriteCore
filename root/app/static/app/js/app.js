new Vue({
  el: '#app',
  data () {
    return {
      allEndpoint:'https://h1rrlt221e.execute-api.us-west-2.amazonaws.com/dev/all_endpoint',
      AutomobileEndpoint:'https://h1rrlt221e.execute-api.us-west-2.amazonaws.com/dev/Automobiles_endpoint/',
      TradingCardsEndpoint:'https://h1rrlt221e.execute-api.us-west-2.amazonaws.com/dev/TradingCards_endpoint/',

      info:null
    }
  },
  mounted () {
    axios
      .get(this.allEndpoint)
      .then(response => (this.info = response.data))
  },
  methods:{
    dataTemplate: function(){
      if(this.info){
        var templateStr=``;
        for (var i = 0; i < this.info.length; i++) {
          templateStr+=`
            <div class="db-item">
              <h1>Risk Type:  ${this.info[i].riskType}</h1>
              <div class=dbidata>
              <h3>Field Name: ${this.info[i].fieldName}</h3>
              <h3>Field Data: ${this.info[i].fieldData}</h3>
              <h3>Field Type: ${this.info[i].fieldType}</h3>
              <h3>Enumerated Type: ${this.info[i].enumType}</h3>
              </div>
            </div>
          `
        }
      return templateStr;

      }
    },

    Endpointall: function(){
      axios.get(this.allEndpoint).then(response => (this.info = response.data))
    },
    Endpointautomobile: function(){
      axios.get(this.AutomobileEndpoint).then(response => (this.info = response.data))
    },
    Endpointtradingcards: function(){
      axios.get(this.TradingCardsEndpoint).then(response => (this.info = response.data))
    }
  }
})