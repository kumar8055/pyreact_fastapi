import React, { Component } from 'react'
import axios from 'axios'
import {Button,Form} from 'react-bootstrap'
import Welcome from './components/Welcome'


class App extends Component{
  constructor(props){
    super(props)

    this.state = {
      ticker : "",
      stock: "msft",
      stocksList: []
    }

    // Binding all functions
    this.createStock = this.createStock.bind(this)
    this.refreshStockList = this.refreshStockList.bind(this)
    this.stockSearch = this.stockSearch.bind(this)
    this.tickerChange = this.tickerChange.bind(this)
  }

  componentDidMount() {
    this.refreshStockList(this.state.stock);
  }

  refreshStockList =  (ticker) =>{
    // ticker = "msft"
    const config =
      {
        "longName": "string",
        "market": "string",
        "phone": "string"
      }
    axios
    .post(`http://localhost:8000/stocks/${ticker}/info`,config)
    .then(res => {  
                  // console.log(res.data);
                  this.setState({stocksList : res.data})
                })
    // .then(res => {console.log(res.data)})
    .catch(err => console.log(err))
  };

  createStock = () =>{
    this.refreshStockList(this.state.ticker)
    const tickers = this.state.stocksList 
    console.log(tickers)
    return tickers
  };

  tickerChange = (event) => {
    event.preventDefault()
    const tkr = event.target.value
    this.setState({ticker:tkr})
    console.log(this.state.ticker)
  }

  stockSearch = (event) =>{
    event.preventDefault()
    // const ticker = this.state.ticker
    this.createStock()
  }

  render(){
    return(
      <div className="App">
      <header className="App-header">
        <Welcome />
        {/* <Button variant="primary" onClick={() => this.createStock("msft")}>{this.state.stocksList.longName}Win</Button> */}
        {/* <Button variant="primary" onClick={this.createStock}> Win</Button> */}
        {/* {this.state.stocksList.longName} */}
        {/* <h1>{this.state.stocksList.map}</h1> */}

        <Form onSubmit={this.stockSearch}>
          <Form.Group>
            <Form.Label>Enter ticker symbol</Form.Label>
            <Form.Control type="text" placeholder="Ticker Symbol" onChange={this.tickerChange}></Form.Control>
          </Form.Group>
          <Button variant="success" type="submit">Stock Info</Button>
        </Form>
      </header>
    </div>
    )
  }
}

export default App;

