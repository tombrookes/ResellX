import React from "react";
import { Line } from "react-chartjs-2";

export default function ProductCard({ product }) {
  return (
    <div className="bg-white shadow-lg rounded-lg p-4">
      <img src={product.image_url} alt={product.name} className="w-full h-48 object-cover mb-2"/>
      <h2 className="text-lg font-semibold">{product.name}</h2>
      <div className="mt-2">
        <Line data={product.priceHistoryChartData} />
      </div>
      <div className="flex justify-between mt-2">
        <span>Avg Sold: ${product.avg_sold_price}</span>
        <span>Lowest Ask: ${product.lowest_ask}</span>
      </div>
      <div className="mt-2 text-sm text-gray-500">
        Most Popular: {product.most_popular_size}
      </div>
      <div className="flex space-x-2 mt-2">
        <button className="bg-green-500 text-white px-3 py-1 rounded">Buy</button>
        <button className="bg-blue-500 text-white px-3 py-1 rounded">Sell</button>
      </div>
    </div>
  );
}