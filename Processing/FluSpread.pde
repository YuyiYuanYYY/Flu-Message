import controlP5.*;

PImage map;

PFont myFont;

Table[] StoPatients;
Table[] FluPatients;
Table FluDayCount;
Table StoDayCount;
Table Weather;
int data = 0;
int flag = 0;
int wind = 0;
PImage[] WordClouds;
PImage[] WindPng;

//Button
ControlP5 cp5;

//Button PNGFile  
PImage[] datePng1;
PImage[] datePng2;

void setup() {
  size(2040, 1400);
  map = loadImage("map.png");
  
  myFont = createFont("Microsoft YaHei", 20);
  textFont(myFont);
  
  StoPatients = new Table[21];
  FluPatients = new Table[21];
  WordClouds = new PImage[21];
  WindPng = new PImage[21];
  
  Weather = loadTable("Weather_new.csv", "header");
  
  for(int row = 0; row < 21; row++) {
    int tmp = 1;
    if(row == 20) {
      tmp = 10;
    }
    StoPatients[row] = loadTable("day_data/"+str(row+tmp)+"/"+str(row+tmp)+"_StomachachePatients.csv", "header");
    FluPatients[row] = loadTable("day_data/"+str(row+tmp)+"/"+str(row+tmp)+"_FluPatients.csv", "header");
    WordClouds[row] = loadImage("day_data/"+str(row+tmp)+"/"+str(row+tmp)+"_WordCloud.png");
    WindPng[row] = loadImage(Weather.getString(row, 6)+".png");
  }
  
  FluDayCount = loadTable("FluDayCount.csv","header");
  StoDayCount = loadTable("StoDayCount.csv","header");
  
  buttonSet();
}

void draw() {
  background(#1D1E31);
  tint(255, 150);
  image(map, 0, 0, 1500, 763); 
  fill(220);
  
  drawBarChart(); 
  drawDate();
  drawPatients();
}

void drawPatients() {
  //Flu
  if(flag == 0) {
    for(int row = 0; row < FluPatients[data].getRowCount(); row++) {
      float lat = FluPatients[data].getFloat(row, 6);
      float lon = FluPatients[data].getFloat(row, 7);
      float x = map(lon, 93.5673, 93.1923, 0, 1500);
      float y = map(lat, 42.3017, 42.1609, 0, 763);
      fill(#FF6021);
      noStroke();
      ellipse(x, y, 10, 10);
      rect(1520, 20, 30, 30);
      textSize(25);
      textAlign(LEFT);
      text("FLu_Like_Patients", 1560, 45);
    }
  }
  
  //Both
  if(flag == 1) {
    for(int row = 0; row < FluPatients[data].getRowCount(); row++) {
      float lat = FluPatients[data].getFloat(row, 6);
      float lon = FluPatients[data].getFloat(row, 7);
      float x = map(lon, 93.5673, 93.1923, 0, 1500);
      float y = map(lat, 42.3017, 42.1609, 0, 763);
      fill(#FF6021);
      noStroke();
      ellipse(x, y, 10, 10);
      rect(1520, 20, 30, 30);
      textSize(25);
      textAlign(LEFT);
      text("FLu_Like_Patients", 1560, 45);
    }
    
    for(int row = 0; row < StoPatients[data].getRowCount(); row++) {
      float lat = StoPatients[data].getFloat(row, 6);
      float lon = StoPatients[data].getFloat(row, 7);
      float x = map(lon, 93.5673, 93.1923, 0, 1500);
      float y = map(lat, 42.3017, 42.1609, 0, 763);
      fill(#12F5CF);
      noStroke();
      ellipse(x, y, 10, 10);
      rect(1520, 70, 30, 30);
      textSize(25);
      textAlign(LEFT);
      text("Stomachache_Like_Patients", 1560, 95);
    }
  }
  
  //Sto
  if(flag == 2) {
    for(int row = 0; row < StoPatients[data].getRowCount(); row++) {
      float lat = StoPatients[data].getFloat(row, 6);
      float lon = StoPatients[data].getFloat(row, 7);
      float x = map(lon, 93.5673, 93.1923, 0, 1500);
      float y = map(lat, 42.3017, 42.1609, 0, 763);
      fill(#12F5CF);
      noStroke();
      ellipse(x, y, 10, 10);
      rect(1520, 70, 30, 30);
      textSize(25);
      textAlign(LEFT);
      text("Stomachache_Like_Patients", 1560, 95);
    }
  }
  
  //Weather
  if(wind == 1) {
    for(int i = 0; i < 5; i++) {
      int x = 1400-i*300;
      int y = 25+i*150;
      image(WindPng[data], x, y, 50, 50);
    }
  }
  
  image(WordClouds[data], 1520, 193, 500, 500);
  
  //Date
  String Time = StoPatients[data].getString(0, 1)+" / "+StoPatients[data].getString(0, 2)+" / "+StoPatients[data].getString(0, 3);
  textSize(50);
  textAlign(CENTER);
  fill(220);
  text(Time, 1770, 760);
  
  //Weather
  String weather = "Weather: "+Weather.getString(data, 3);
  text(weather, 1770, 175);
}

void drawDate() {
  //calendar
  textSize(25);
  fill(220);
  text("Mon", 1520, 830);
  text("Tue", 1595, 830);
  text("Wed", 1670, 830);
  text("Thu", 1745, 830);
  text("Fri", 1820, 830);
  text("Sat", 1895, 830);
  text("Sun", 1970, 830);  
}


void drawBarChart() {  
  stroke(150);
  strokeWeight(2);
  line(80, 780, 80, 1350);
  line(80, 1350, 1480, 1350);
  
  for(int i = 0; i < 5; i++) {
    int num = 0;
    num = i*5000;
    textSize(20);
    textAlign(RIGHT);
    text(str(num), 70, 1350-140*i);
    line(80, 1350-142*i, 85, 1350-142*i);
  }
  
  for(int col1 = 1; col1 < FluDayCount.getColumnCount(); col1++) {    
    fill(150);
    textAlign(CENTER);
    text(FluDayCount.getColumnTitle(col1), 125 + 65*(col1-1), 1380);
    
    noStroke();
    float h = 0;
    for(int row1 = 0; row1 < FluDayCount.getRowCount(); row1++) {      
      float r1 = map(row1, 0, float(FluDayCount.getRowCount() - 1), 255, 163);
      float g1 = map(row1, 0, float(FluDayCount.getRowCount() - 1), 185, 73);
      float b1 = map(row1, 0, float(FluDayCount.getRowCount() - 1), 137, 10);
      fill(r1, g1, b1);
      
      rect(105, 1000 - 40*(row1-1), 25, 25);
      textAlign(LEFT);
      text(FluDayCount.getString(row1, 0), 140, 1020 - 40*(row1-1));
      
      float rect_h1 = map(FluDayCount.getFloat(row1, col1), 0, 20000, 0, 580);
      h += rect_h1;
      rect(105 + 65*(col1-1), 1350-h, 35, rect_h1);
    }
    
      
    for(int row2 = 0; row2 < StoDayCount.getRowCount(); row2++) {
      float r2 = map(row2, 0, float(StoDayCount.getRowCount() - 1), 194, 0);
      float g2 = map(row2, 0, float(StoDayCount.getRowCount() - 1), 255, 168);
      float b2 = map(row2, 0, float(StoDayCount.getRowCount() - 1), 245, 140);
      fill(r2, g2, b2);
      
      rect(280, 1000 - 40*(row2-1), 25, 25);
      text(StoDayCount.getString(row2, 0), 315, 1020 - 40*(row2-1));
      
      float rect_h2 = map(StoDayCount.getFloat(row2, col1), 0, 20000, 0, 580);
      h += rect_h2;
      rect(105 + 65*(col1-1), 1350-h, 35, rect_h2);
    }
  }
}

void buttonSet() {  
  cp5 = new ControlP5(this);
  String[] dateBtn = new String[21];
  PImage[] datePng1 = new PImage[21];
  PImage[] datePng2 = new PImage[21];
  
  for(int i = 0; i < 21; i++) {
    int tmp = 1;
    if(i == 20) {
      tmp = 10;
    }
    dateBtn[i] = "date" + Integer.toString(i+tmp);
    datePng1[i] = loadImage("date" + Integer.toString(i+tmp) + "_1.png");
    datePng2[i] = loadImage("date" + Integer.toString(i+tmp) + "_2.png");
  }
  
  tint(255, 255);
  int week = 6;
  int day = 6;
  for(int i = 0; i < 21; i++) {
    if(i == 20) {
      cp5.addButton(dateBtn[i])
      .setValue(0)
      .setPosition(1895, 860)
      .setImages(datePng1[i], datePng1[i], datePng2[i])
      .updateSize();
    }
    
    else {
      day = day%7;
      int x = 1520 + day*75;
      int y = 860 + week/7*100;
      cp5.addButton(dateBtn[i])
        .setValue(0)
        .setPosition(x, y)
        .setImages(datePng1[i], datePng1[i], datePng2[i])
        .updateSize();
      day++;
      week++;
    }    
  }
  cp5.addButton("Flu")
    .setValue(0)
    .setPosition(1520, 1250)
    .setImages(loadImage("Flu1.png"), loadImage("Flu1.png"), loadImage("Flu2.png"))
    .updateSize();
  
  cp5.addButton("Stomache")
    .setValue(0)
    .setPosition(1820, 1250)
    .setImages(loadImage("Sto1.png"), loadImage("Sto1.png"), loadImage("Sto2.png"))
    .updateSize();
    
  cp5.addButton("Both")
    .setValue(0)
    .setPosition(1670, 1250)
    .setImages(loadImage("Both1.png"), loadImage("Both1.png"), loadImage("Both2.png"))
    .updateSize();
    
  cp5.addButton("Wind")
    .setValue(0)
    .setPosition(1520, 1320)
    .setImages(loadImage("Wind1.png"), loadImage("Wind1.png"), loadImage("Wind2.png"))
    .updateSize();
}

void date1() {
  data = 0;
}

void date2() {
  data = 1;
}

void date3() {
  data = 2;
}

void date4() {
  data = 3;
}

void date5() {
  data = 4;
}

void date6() {
  data = 5;
}

void date7() {
  data = 6;
}

void date8() {
  data = 7;
}

void date9() {
  data = 8;
}

void date10() {
  data = 9;
}

void date11() {
  data = 10;
}

void date12() {
  data = 11;
}

void date13() {
  data = 12;
}

void date14() {
  data = 13;
}

void date15() {
  data = 14;
}

void date16() {
  data = 15;
}

void date17() {
  data = 16;
}

void date18() {
  data = 17;
}

void date19() {
  data = 18;
}

void date20() {
  data = 19;
}

void date30() {
  data = 20;
}

void Flu() {
  flag = 0;
}

void Stomache() {
  flag = 2;
}

void Both() {
  flag = 1;
}

void Wind() {
  if(wind == 0) {
    wind = 1;
  }
  else {
    wind = 0;
  }
}
