
library(ggplot2)

# Create a ggplot object
p <- ggplot(data, aes(x=x_var, y=y_var)) + geom_point()

# Display the plot
print(p)

# Save the plot to a file
ggsave("item_sales_quantity.png", plot = p, width = 7, height = 7, units = "in")
