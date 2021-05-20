import React, { Component } from 'react';
import { Line } from 'react-chartjs-2';
// import classes from './MyChart.module.css'

const state = {
    // labels: ['January', 'February', 'March', 'April', 'May'],
    // labels: ["2017-01-03T00:00:00","2017-01-04T00:00:00","2017-01-05T00:00:00","2017-01-06T00:00:00","2017-01-09T00:00:00","2017-01-10T00:00:00","2017-01-11T00:00:00","2017-01-12T00:00:00","2017-01-13T00:00:00","2017-01-17T00:00:00","2017-01-18T00:00:00","2017-01-19T00:00:00","2017-01-20T00:00:00"],
    labels:[],
    datasets: [
        {
            label: 'Stocks',
            fill: false,
            lineTension: 0.5,
            backgroundColor: 'rgba(75,192,192,1)',
            borderColor: 'rgba(0,0,0,1)',
            borderWidth: 2,
            // data: [65, 59, 80, 81, 56]
            data: [28.950000762939453,28.962499618530273,28.979999542236328,29.19499969482422,29.487499237060547,29.6924991607666,29.684999465942383,29.725000381469727,29.77750015258789,29.584999084472656,30,29.850000381469727,30.112499237060547]
            // data:
        }
    ]
}

export default class App extends React.Component {
    render() {
        return (
            <div>
                
                        <Line
                    data={state}
                    options={{
                        title: {
                            display: true,
                            text: 'Average Rainfall per month',
                            fontSize: 20
                        },
                        legend: {
                            display: true,
                            position: 'right'
                        }
                    }}
                />
            </div>
        );
    }
}