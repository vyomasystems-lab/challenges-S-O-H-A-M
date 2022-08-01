module UniversalShiftRegister(input [3:0] b,input clk,s1,s0,r_in,l_in,output[3:0] y,q);

mux m1(s1,s0,{b[3],q[2],r_in,q[3]},y[3]); //for 4 inputs used concatenation operator
d_ff d1(y[3],clk,q[3]);

mux m2(s1,s0,{b[2],q[1],q[3],q[2]},y[2]);
d_ff d2(y[2],clk,q[2]);

mux m3(s1,s0,{b[1],q[0],q[2],q[1]},y[1]);
d_ff d3(y[1],clk,q[1]);

mux m4(s1,s0,{b[0],l_in,q[1],q[0]},y[0]);
d_ff d4(y[0],clk,q[0]);

endmodule

module mux(input s1,s0,input [3:0] b,output reg y);

always @(s1 or s0) 
begin

case({s1,s0})

2'b00:begin y=b[0]; end
2'b01:begin y=b[1]; end
2'b10:begin y=b[2]; end
2'b11:begin y=b[3]; end

endcase
end
endmodule

module d_ff(input d,clk,output reg q);

always @(posedge clk)
begin
    q=d;
end

endmodule

