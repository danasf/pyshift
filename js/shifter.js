/*
Bonescript shift register test. Very experimental....
BBB pinout: http://insigntech.files.wordpress.com/2013/09/bbb_pinouts.jpg
2 data lines, 3 selectors, oe, clock and latch
*/

function Matrix(b,data1,data2,clk,lat,s1,s2,s3,oe) {
	// vars to local
	this.b = b;
	this.clk = clk;
	this.latch = lat;
	this.oe = oe;
	this.r1 = data1;
	this.r2 = data2;

	// matrix details
	this.x = 32;
	this.y = 16;

	// select bits
	this.s1 = s1;
	this.s2 = s2;
	this.s3 = s3;

	// set as out
	this.b.pinMode(this.clk, 'out');
	this.b.pinMode(this.latch, 'out');
	this.b.pinMode(this.oe, 'out');
	this.b.pinMode(this.r1, 'out');
	this.b.pinMode(this.r2, 'out');
	this.b.pinMode(this.s1, 'out');
	this.b.pinMode(this.s2, 'out');
	this.b.pinMode(this.s3, 'out');

	// write some init values
	this.b.digitalWrite(this.clk,this.b.HIGH);
	this.b.digitalWrite(this.latch,this.b.HIGH);
	this.b.digitalWrite(this.oe,this.b.LOW);

	// set selection bits
	this.b.digitalWrite(this.s1,this.b.LOW);
	this.b.digitalWrite(this.s2,this.b.LOW);
	this.b.digitalWrite(this.s3,this.b.LOW);



};

// select position 0, 7

Matrix.prototype.setRow = function(row) {
	if(row > 7) { row = row - 8; }
	if(row === 0) {
		this.sel(0,0,0);
	}
	else if (row === 1) {
		this.sel(0,0,1);
	}
	else if (row === 2) {
		this.sel(0,1,0);
	}
	else if (row === 3) {
		this.sel(0,1,1);
	}
	else if (row === 4) {
		this.sel(1,0,0);
	}
	else if (row === 5) {
		this.sel(1,0,1);
	}
	else if (row === 6) {
		this.sel(1,1,0);
	}
	else if (row === 7) {
		this.sel(1,1,1);
	} else {
		this.sel(0,0,0);
	}

}

Matrix.prototype.sel = function(s1,s2,s3) {

		this.b.digitalWrite(this.oe, this.b.HIGH);
		this.b.digitalWrite(this.s1,s1);
		this.b.digitalWrite(this.s2,s2);
		this.b.digitalWrite(this.s3,s3);
		this.b.digitalWrite(this.oe, this.b.LOW);

};

// set a single bit
Matrix.prototype.setBit = function(pin,state) {
	this.b.digitalWrite(pin,state);
	this.b.digitalWrite(this.clk,this.b.LOW);
	this.b.digitalWrite(this.clk,this.b.HIGH);
};

// fill an array of bits
Matrix.prototype.bitFill = function(pin,num,callback) {
	for (var i = num+1; i >= 0; i--) {
		this.setBit(pin,this.b.HIGH);
	}
	for (var i = this.x-num; i >= 0; i--) {
		this.setBit(pin,this.b.LOW);
	}
	callback();
};

// latch
Matrix.prototype.latchData = function() {
	 this.b.digitalWrite(this.oe, this.b.HIGH);
	 this.b.digitalWrite(this.latch, this.b.HIGH);
	 this.b.digitalWrite(this.latch, this.b.LOW);
	 this.b.digitalWrite(this.oe, this.b.LOW);

};

/// start script

function rowHelper(row) {
	return (row > 7) ? mat.r2 : mat.r1;
};

var b = require('bonescript');

// new matrix b, data1, data2, clock, lat, selA, selB, selC, OE
var mat = new Matrix(b,"P8_7","P8_13","P8_9","P8_11","P8_8","P8_10","P8_12","P8_14");
while (1 == 1) {

	/*// scan down
	for(var x=0; x < 15; x++) { 
		mat.bitFill(rowHelper(x),32,function() {
			mat.setRow(x);
		});
	}
	mat.latchData();

	// scan up
	for(var x=15; x > 0; x--) { 
		mat.bitFill(rowHelper(x),32,function() {
			mat.latchData();
			mat.setRow(x);
		});
	}*/
	// push in some bits
    for(var i=0; i < 8; i++) {
            mat.setRow(i);
            mat.setBit(mat.r1,1);
            mat.setBit(mat.r1,1);
            mat.setBit(mat.r1,0);
            mat.setBit(mat.r1,0);
            mat.latchData();
    }
}

