# MultiNets: Multiplex Convolutional Visibility Graph Networks for Multivariate Carbon Price Forecasting
![PyTorch Badge](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=fff&style=plastic)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=plastic)
![pandas Badge](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=fff&style=plastic)
![scikit-learn Badge](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=fff&style=plastic)
![Apache Badge](https://img.shields.io/badge/Apache-D22128?logo=apache&logoColor=fff&style=plastic)

This repo is the implementation and related sources of MultiNets, which investigates multivariate carbon prices by a novel graph representation of visibility network, and develops multivariate forecasting frameworks. 

<p align="center">
<img src="https://github.com/szmao1/MultiNets/blob/main/img/1multiplex.png" height = "200" alt="" align=center />
<p style="text-align: left;">
<b>Fig. 1</b> The construction of multiplex visibility graph. Each variable representing the impact factor associated with carbon data is transformed into an individual graph.
</p>


## Main Features
### External factors
Carbon price tends to be affected by not only intrinsic market mechanisms but also a myriad of extrinsic complex ingredients like energy influences and economic indicators as presented in Fig. 2. To investigate the relationships between carbon price and extraneous variables precisely, we implement Pearson correlation test and the coefficients are shown in Fig. 3. As can be seen, all factors are positively associated with carbon data, at least having an over 0.6 correlation and most over 0.8.



<table>
  <tr>
    <td align="center">
      <img src="https://github.com/szmao1/MultiNets/blob/main/img/2factors.png" width="275"/>
      <p>
      <p><b>Fig. 2</b> External impact factors.</p>
    </td>
    <td align="center">
      <img src="https://github.com/szmao1/MultiNets/blob/main/img/3heatmap.png" width="190"/>
      <p><b>Fig. 3</b> The heatmap of Pearson correlation.</p>
    </td>
  </tr>
</table>

The energy prices are plotted in red shown below and economic indexes are in green. It can be found that all the external indicators witness a sharp fluctuation especially during COVID-19, except for Rotterdam coal futures prices, which remained flat while surging in the second half of 2021 due to the European energy crisis.

<div align="center">
  <img src="https://github.com/szmao1/MultiNets/blob/main/img/10plotfactor.png" height="400"/>
  <p><b>Fig. 4</b> Two groups of impact factors related to carbon price.</p>
</div>


### Address information loss
Visibility graph encoding offers a prospective strategy for sequence representation, while it suffers from two drawbacks: **(i) loss of value information**, and **(ii) loss of temporal correlations**. Therefore, we propose a weighted graph presentation technique to overcome the information loss by introducing a weight parameter, in order to inherit price features as well as capture correlations across timestamps

<div align="center">
  <img src="https://github.com/szmao1/MultiNets/blob/main/img/4loss.png" height="250"/>
  <p><b>Fig. 5</b> The weight parameter
is introduced between any two nodes.</p>
</div>


### SimLayer: Layer Similarity
By analyzing the intra-layer similarity,
we explore the temporal dependencies and patterns
within individual layers, which reflect the dynamics of a single
influencing factor. In contrast, the inter-layer similarity
analysis quantifies the relationships between corresponding
nodes across different layers, capturing the complex interactions
between multiple variables. 


<table>
  <tr>
    <td align="center">
      <img src="https://github.com/szmao1/MultiNets/blob/main/img/5prob.png" width="300"/>
      <p><b>Fig. 6</b> The probability distribution in the network.</p>
    </td>
    <td align="center">
      <img src="https://github.com/szmao1/MultiNets/blob/main/img/6feature.png" width="320"/>
      <p><b>Fig. 7</b> The aggregated intra-similarity.</p>
    </td>
  </tr>
</table>

## Results
### Multivarite forecasting
* MultiNets outperformed all baselines including econometric, machine learning and hybrid methods, with the best metrics in terms of MAE, RMSE, and MAPE.

* EMD-MultiNets and MEMD-MultiNets further improved results, with MEMD-MultiNets achieving the best overall performance.

* EMD and MEMD enhanced MultiNets, with MEMD showing the greatest improvement in capturing complex data relationships.

  <div align="center">
  <img src="https://github.com/szmao1/MultiNets/blob/main/img/7multiresults.png" height="300"/>
  <p><b>Fig. 8</b> The forecasting results of three categories of baselines as well as proposed model named MultiNets and the variants EMD-MultiNets and MEMD-MultiNets by integrating EMD and MEMD into MultiNets. The best predictive results are highlighted in bold.</p>
</div>
  
### Univariate Forecasting

* It successfully captured complex patterns in single-variable carbon price data.

* When tested on datasets like DEC15 and DEC16, MultiNets outperformed traditional and hybrid models, dealing well with the nonlinearities and in the data.

* MultiNets is a powerful tool for both multivariate and univariate forecasting tasks, leveraging graph-based visibility networks and CNNs effectively.

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/szmao1/MultiNets/blob/main/img/8uniresults.png" width="300"/>
      <p><b>Fig. 9</b> Univariate forecasting of hybrid models and MultiNets.</p>
    </td>
    <td align="center">
      <img src="https://github.com/szmao1/MultiNets/blob/main/img/9ablation.png" width="300"/>
      <p><b>Fig. 10</b> The experimental results of ablation study.</p>
    </td>
  </tr>
</table>

## Requirements
* numpy == 1.19.1
* torch == 1.8.0
* pandas
* scikit_learn
* matplotlib
* statsmodels==0.13.2
* NetworkX

## Contact
If you have any questions or concerns, please feel free to contact Shengzhong through the email: shengzhong.mao@manchester.ac.uk or submit an issue.

## Acknowledgement
The authors would like to thank the President’s Doctoral Scholar Award at the University of Manchester to support this work.
