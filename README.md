# Dither-by-Four-Gray-Values

> Author : Ya Chen <br />
> Date : 2021 / 3 / 19

---

# Description

- <font size = 4px>Step 1 : </font> &emsp;
  255 / 3 = 85
- <font size = 4px>Step 2 : </font> &emsp;
  Q ( i, j ) = [ I ( i, j ) / 85]
- <font size = 4px>Step 3 : </font> <br>
  <b>D<sub>1</sub></b> =
  <table>
    <tr>
        <td>0</td>
        <td>56</td>
    </tr>
    <tr>
        <td>84</td>
        <td>28</td>
    </tr>
  </table>
  <br>
  <b>D =</b>
  <table border = "1">
      <tr>
        <td>D<sub>1</sub></td>
        <td>D<sub>1</sub></td>
        <td>D<sub>1</sub></td>
        <td>...
        <td>D<sub>1</sub></td>
      <tr>
        <td>D<sub>1</sub></td>
        <td>D<sub>1</sub></td>
        <td>D<sub>1</sub></td>
        <td>...
        <td>D<sub>1</sub></td>
      <tr>
        <td>
        <td>...
        <td>
        <td>
        <td>...
      <tr>
        <td>D<sub>1</sub></td>
        <td>D<sub>1</sub></td>
        <td>D<sub>1</sub></td>
        <td>...
        <td>D<sub>1</sub></td>
   </table>

- <font size = 4px>Step 4 : </font>
    <table border = "0">
      <tr>
        <td>I ' ( i , j ) =
        <td>Q ( i , j ) +
        <td>{
        <td>1
        <td>if  I ( i , j ) - 85 x Q ( i , j ) >  D ( i , j )
      <tr>
        <td>
        <td>
        <td>{
        <td>0
        <td>if  I ( i , j ) - 85 x Q ( i , j ) < =  D( i , j )
   </table>
- <font size = 4px>Step 5 : </font> &emsp;
  <font size = 3px>Scale values of I' so that its values are in [ 0, 255 ] for displaying </font>
