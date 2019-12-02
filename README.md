# brand_matching
The goal here is to try a matching algorithm to be able to suggest a Sub-Brand for Articles that are missing Sub-Brand and enable User Feedback to improve the suggestions.
<html xmlns:o=3D"urn:schemas-microsoft-com:office:office"
xmlns:dt=3D"uuid:C2F41010-65B3-11d1-A29F-00AA00C14882"
xmlns=3D"http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=3DContent-Type content=3D"text/html; charset=3Dutf-8">
<meta name=3DProgId content=3DOneNote.File>
<meta name=3DGenerator content=3D"Microsoft OneNote 15">
<link id=3DMain-File rel=3DMain-File href=3DMethod.htm>
<link rel=3DFile-List href=3D"Method_files/filelist.xml">
</head>

<body lang=3Den-US style=3D'font-family:Calibri;font-size:11.0pt'>

<div style=3D'direction:ltr;border-width:100%'>

<div style=3D'direction:ltr;margin-top:0in;margin-left:0in;width:9.9979in'>

<div style=3D'direction:ltr;margin-top:0in;margin-left:.3312in;width:1.4493=
in'>

<p style=3D'margin:0in;font-family:"Calibri Light";font-size:20.0pt'>Method=
</p>

</div>

<div style=3D'direction:ltr;margin-top:.0388in;margin-left:.3312in;width:2.=
5826in'>

<p style=3D'margin:0in;font-family:Calibri;font-size:10.0pt;color:#767676'>=
Monday,
December 2, 2019</p>

<p style=3D'margin:0in;font-family:Calibri;font-size:10.0pt;color:#767676'>=
12:09
PM</p>

</div>

<div style=3D'direction:ltr;margin-top:.4305in;margin-left:0in;width:9.9979=
in'>

<ul style=3D'margin-left:.3097in;direction:ltr;unicode-bidi:embed;margin-to=
p:
 0in;margin-bottom:0in'>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA><span style=3D'font-style:italic'>Suggested Qualifier - Brand=
s with
 Sub-brand</span>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <ul type=3Ddisc style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;
  margin-top:0in;margin-bottom:0in'>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Par=
se the
      data into two frames, one where the Sub-Brands are populated and one
      where Sub-Brands are null&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Ite=
rate
      through&nbsp;</span><span style=3D'font-weight:bold;font-family:Calib=
ri;
      font-size:11.0pt'>One Brand</span><span style=3D'font-family:Calibri;
      font-size:11.0pt'>&nbsp;at a time i.e. Cluster a particular Brand with
      all it's articles in the Null dataframe&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>For=
 each
      null record for Sub-Brand in this Brand Cluster&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Use=
 one of
      the algorithms from Jellyfish to find the highest match using Article
      Description on the dataframe where Sub-Brand is populated&nbsp;</span=
></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Jar=
o-Winkler&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Jaro
      Distance&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Lev=
enshtein
      Distance&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Dam=
erau-Levenshtein
      Distance&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Ass=
ign the
      Sub-Brand that is attached to the highest matched Article
      Description&nbsp;</span></li>
 </ul>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>Check against Existing Brand/Sub-Brand relationships in the t=
able
 ZMD_SUBBRAND_MAP, do not assign a Sub-Brand that does not share a relation=
ship
 with the Brand in question&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA><span style=3D'font-weight:bold'>In order to retrieve feedbac=
k from a
 user, the output file must have a column to capture the following</span>&n=
bsp;</p>
 <ul type=3Ddisc style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;
  margin-top:0in;margin-bottom:0in'>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>A (=
Accept -
      Accept Sub-Brand)&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>RW =
(Reject
      - Wrong Sub-Brand)&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>RN =
(Reject
      - No Sub-Brand)&nbsp;</span></li>
 </ul>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>Please ensure that Article Number and UPC is part of the
 output.&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'><=
span
 lang=3Den-CA>Once the user has finished the feedback i</span><span lang=3D=
en-US>ngest
 this file and for the next iteration of suggestions filter out where user =
has
 indicated&nbsp;</span><span style=3D'font-weight:bold' lang=3Den-US>RN</sp=
an><span
 lang=3Den-US>&nbsp;- Reject - No Sub-Brand so those suggestions are never
 brought to the user's attention again.</span><span lang=3Den-CA>&nbsp;</sp=
an></p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>
 <p style=3D'margin:0in'><img src=3D"Method_files/image001.png" width=3D926
 height=3D738
 alt=3D"Sequential Approach &#10;Article M ach &#10;Article M ach &#10;Foun=
d ? &#10;Sub-brand &#10;LlÃ¦ Article M ach &#10;Match &#10;&amp; op &#10;Pa=
rallel Approach &#10;Article M ach &#10;Sub-brand M ach &#10;Article M ach =
&#10;Found ? &#10;Article M ach &#10;Sub-brand &#10;sam e Su &#10;Match &#1=
0;and Mach &#10;Report both &#10;mach r sults for &#10;user review &#10;LlÃ=
¦ the agr Ã¦d &#10;result"></p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt'>&nbsp;</p>
 <ol type=3D1 style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;mar=
gin-top:
  0in;margin-bottom:0in;font-family:Calibri;font-size:11.0pt;font-weight:no=
rmal;
  font-style:normal'>
  <li value=3D1 style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;
      color:black' lang=3Den-CA><span style=3D'font-family:Calibri;font-siz=
e:11.0pt;
      font-weight:normal;font-style:normal;font-family:Calibri;font-size:11=
.0pt'>Terminology:&nbsp;</span></li>
 </ol>
 <ul type=3Ddisc style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;
  margin-top:0in;margin-bottom:0in'>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Art=
icle
      match : Matching performed against other article descriptions. Result=
 is
      sub-brand of the closest article description match.&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Sub=
-brand
      match : Matching performed against the sub-brand name itself. Result =
is
      that of the closest sub-brand name match.&nbsp;</span></li>
 </ul>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <ol type=3D1 style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;mar=
gin-top:
  0in;margin-bottom:0in;font-family:Calibri;font-size:11.0pt;font-weight:no=
rmal;
  font-style:normal'>
  <li value=3D2 style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;
      color:black' lang=3Den-CA><span style=3D'font-family:Calibri;font-siz=
e:11.0pt;
      font-weight:normal;font-style:normal;font-family:Calibri;font-size:11=
.0pt'>Methodology
      :&nbsp;</span></li>
 </ol>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>2.1. Filter :&nbsp;</p>
 <ul type=3Ddisc style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;
  margin-top:0in;margin-bottom:0in'>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>For=
 article
      match : Compare only with articles of the same brand and belong to the
      same category (based on Category.xlsx)&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>For
      sub-brand match : Compare only with sub-brands of the same brand
      (ZMD_SUBBRAND_MAP.xlsx)&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>&nb=
sp;&nbsp;</span></li>
 </ul>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>2.2. Matching score :&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>Based on our own experiments and research results from the
 industry, we observed that Levenshtein-based and Hamming matching algorith=
ms
 are not good choices in our use-case. The two remaining candidates for
 matching score that we consider are :&nbsp;</p>
 <ul type=3Ddisc style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;
  margin-top:0in;margin-bottom:0in'>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Rat=
cliff/Obershelp&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Jar=
o-Winkler&nbsp;</span></li>
 </ul>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>2.3. Approach :&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>There is no obvious winner in the approaches attempted. We wi=
ll
 therefore report several approaches to provide users with a rich choice for
 assessment.&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <ol type=3D1 style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;mar=
gin-top:
  0in;margin-bottom:0in;font-family:Calibri;font-size:11.0pt;font-weight:no=
rmal;
  font-style:normal'>
  <li value=3D3 style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;
      color:black' lang=3Den-CA><span style=3D'font-family:Calibri;font-siz=
e:11.0pt;
      font-weight:normal;font-style:normal;font-family:Calibri;font-size:11=
.0pt'>Sequential
      approach:&nbsp;</span></li>
 </ol>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>Inspired by the approach used in v1.0:&nbsp;</p>
 <ul type=3Ddisc style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;
  margin-top:0in;margin-bottom:0in'>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Ste=
p 1 :
      Perform article match&nbsp;&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>If =
the
      resulting sub-brand of the matching description exist, consider this =
as a
      result&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Oth=
erwise,
      move to step 2&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Ste=
p 2:
      Perform sub-brand match. Return the result of this sub-brand match&nb=
sp;</span></li>
 </ul>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <ol type=3D1 style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;mar=
gin-top:
  0in;margin-bottom:0in;font-family:Calibri;font-size:11.0pt;font-weight:no=
rmal;
  font-style:normal'>
  <li value=3D4 style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;
      color:black' lang=3Den-CA><span style=3D'font-family:Calibri;font-siz=
e:11.0pt;
      font-weight:normal;font-style:normal;font-family:Calibri;font-size:11=
.0pt'>Parallel
      approach :&nbsp;</span></li>
 </ol>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>Report article match result and sub-brand match result separa=
tely
 and independently of each other.&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>Consolidation:&nbsp;&nbsp;</p>
 <ul type=3Ddisc style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;
  margin-top:0in;margin-bottom:0in'>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>If =
article
      match result is not found, report sub-brand match as the final result
      (similar logic to sequential approach)&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Els=
e, if
      article match result is the same as sub-brand match result, report th=
is
      as the final result&nbsp;&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Oth=
erwise,
      if both match results exist but are different, report both and let us=
ers
      decide.&nbsp;</span></li>
 </ul>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <ol type=3D1 style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;mar=
gin-top:
  0in;margin-bottom:0in;font-family:Calibri;font-size:11.0pt;font-weight:no=
rmal;
  font-style:normal'>
  <li value=3D5 style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;
      color:black' lang=3Den-CA><span style=3D'font-family:Calibri;font-siz=
e:11.0pt;
      font-weight:normal;font-style:normal;font-family:Calibri;font-size:11=
.0pt'>Interface
      design for user feedback:&nbsp;</span></li>
 </ol>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>Manage 2 Excel files :&nbsp;</p>
 <ul type=3Ddisc style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;
  margin-top:0in;margin-bottom:0in'>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Act=
ive file
      : All articles that require user review.&nbsp;Based on the match resu=
lt
      proposed :&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>If =
the
      match result is A (Accepted) : Good match; to be removed from list&nb=
sp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>If =
the
      match result is RW (Rejected wrong) : User makes correction in SAP.&n=
bsp;
      Article is also removed from list&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>If =
the
      match result is RN (Rejected Not needed): Remove article from Active =
file
      and move to Inactive file&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Ina=
ctive
      file : All articles marked as &quot;Sub-brand not needed&quot; by use=
r,
      to be removed consideration for next iteration. These articles are
      removed from Active file and moved to Inactive file&nbsp;</span></li>
 </ul>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>The process will be automated (daily, weekly, etc.) to take u=
ser
 feedback and split into two files as mentioned above.&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA><span style=3D'font-weight:bold;text-decoration:underline'>Co=
lumns to
 be reported :</span>&nbsp;</p>
 <ul type=3Ddisc style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;
  margin-top:0in;margin-bottom:0in'>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>SAP=
_Article_Number&nbsp;&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>SAP=
_GTIN&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>SAP=
_Article_Description&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>CPM=
S_Descr&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>SAP=
_MCH0&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>SAP=
_MCH0_Descr&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>SAP=
_Brand&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>SAP=
_Brand_Description&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>sub=
brand_text
      =3D&gt; seq_sub_brand_out&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>sub=
brand_res
      =3D&gt;&nbsp;seq_sub_brand_res&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Par=
allel_sub_brand_1_out&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Par=
allel_match_desc_Ratcliff&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Par=
allel_sub_brand_2_out&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Par=
allel_match_subbrand_Ratcliff&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Fee=
dback&nbsp;</span></li>
 </ul>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA><span style=3D'font-weight:bold;text-decoration:underline'>Gl=
ossary
 of results (subbrand_out.xlsx)</span>&nbsp;</p>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>Sequential Approach :&nbsp;</p>
 <ul type=3Ddisc style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;
  margin-top:0in;margin-bottom:0in'>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>sub=
brand_text
      : Final result of Sequential Approach&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>sub=
brand_res
      : Details decision making of Sequential Approach â€“ sub-brand result,
      matching score, top description match&nbsp;</span></li>
 </ul>
 <p style=3D'margin:0in;font-family:Calibri;font-size:11.0pt;color:black'
 lang=3Den-CA>Parallel Approach :&nbsp;</p>
 <ul type=3Ddisc style=3D'margin-left:0in;direction:ltr;unicode-bidi:embed;
  margin-top:0in;margin-bottom:0in'>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>des=
c_subbrand_agreement_Ratcliff
      : Agreement between article match and sub-brand match for Ratcliff
      metric&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>mat=
ch_desc_Ratcliff
      : Best match when using article match. Ratcliff metric&nbsp;</span></=
li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>mat=
ch_subbrand_Ratcliff
      :&nbsp;Best match when using sub-brandmatch. Ratcliff metric&nbsp;</s=
pan></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>des=
c_subbrand_agreement_Jaro_winkler
      :&nbsp;Agreement between article match and sub-brand match for
      Jaro-Winkler metric&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>mat=
ch_desc_Jaro_winkler
      : Best match when using article
      match.&nbsp;Jaro-winkler&nbsp;metric&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>mat=
ch_subbrand_Jaro_winkler&nbsp;:&nbsp;Best
      match when using sub-brandmatch.&nbsp;Jaro-winkler&nbsp;metric&nbsp;<=
/span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Add=
itional
      column match_desc_Hamming : Best match when using article match. Hamm=
ing
      metric&nbsp;</span></li>
  <li style=3D'margin-top:0;margin-bottom:0;vertical-align:middle;color:bla=
ck'
      lang=3Den-CA><span style=3D'font-family:Calibri;font-size:11.0pt'>Add=
itional
      column match_subbrand_Hamming :&nbsp;Best match when using
      sub-brandmatch. Hamming metric&nbsp;</span></li>
 </ul>
</ul>

</div>

</div>

</div>

<div>

<p style=3D'margin:0in'>&nbsp;</p>

<p style=3D'text-align:left;margin:0in;font-family:Arial;font-size:9pt;
color:#969696;direction:ltr'>Created with Microsoft OneNote 2016.</p>

</div>

</body>

</html>
