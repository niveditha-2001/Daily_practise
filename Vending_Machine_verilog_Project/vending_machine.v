module vending_machine (
    input clk,
    input reset,
    input [3:0] money_in,
    input [2:0] product_code,   // 3 bits (0-7)
    output reg dispense,
    output reg [3:0] change,
    output reg out_of_stock
);

    reg [3:0] product_price;

    // Stock count for each product (6 products)
    reg [3:0] stock [0:5];

    // Combinational block to determine product price
    always @(*) begin
        case (product_code)
            3'b000: product_price = 4'd15;
            3'b001: product_price = 4'd5;
            3'b010: product_price = 4'd10;
            3'b011: product_price = 4'd5;
            3'b100: product_price = 4'd5;
            3'b101: product_price = 4'd10;
            default: product_price = 4'd15;
        endcase
    end

    // Sequential block for vending machine logic
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            stock[0] <= 4'd10;
            stock[1] <= 4'd0;
            stock[2] <= 4'd3;
            stock[3] <= 4'd1;
            stock[4] <= 4'd5;
            stock[5] <= 4'd8;

            dispense <= 0;
            change <= 0;
            out_of_stock <= 0;
        end else begin
            if (product_code <= 5) begin
                if (stock[product_code] == 0) begin
                    dispense <= 0;
                    change <= money_in;
                    out_of_stock <= 1;
                end else if (money_in >= product_price) begin
                    dispense <= 1;
                    change <= money_in - product_price;
                    out_of_stock <= 0;
                    stock[product_code] <= stock[product_code] - 1;
                end else begin
                    dispense <= 0;
                    change <= money_in;
                    out_of_stock <= 0;
                end
            end else begin
                dispense <= 0;
                change <= money_in;
                out_of_stock <= 1;
            end
        end
    end

    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0, vending_machine);
    end

endmodule
