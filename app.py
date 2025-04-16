
import React from 'react';
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ComposedChart, LabelList } from 'recharts';

const FinancialDashboard = () => {
  const data = [
    { year: '2025', revenue: 2.4, cost: 6.5, profit: -4.1, devCost: 5.5, marketing: 1, operations: 0.5, other: 0, restaurants: 100 },
    { year: '2026', revenue: 12, cost: 4, profit: 8, devCost: 0, marketing: 2, operations: 1, other: 1, restaurants: 500 },
    { year: '2027', revenue: 36, cost: 5, profit: 31, devCost: 0, marketing: 3, operations: 1.5, other: 0.5, restaurants: 1500 }
  ];

  let cumulativeProfit = 0;
  let cumulativeCost = 0;
  const roiData = data.map((item, index) => {
    const annualProfit = item.profit;
    const annualCost = item.cost;

    cumulativeProfit += annualProfit;
    cumulativeCost += annualCost;

    return {
      year: item.year,
      roi: +(annualProfit / annualCost * 100).toFixed(1),
      cumulativeRoi: +(cumulativeProfit / cumulativeCost * 100).toFixed(1)
    };
  });

  const costBreakdownData = [
    { name: 'Dev Cost', 2025: 5.5, 2026: 0, 2027: 0 },
    { name: 'Marketing & Sales', 2025: 1, 2026: 2, 2027: 3 },
    { name: 'Operations', 2025: 0.5, 2026: 1, 2027: 1.5 },
    { name: 'Other', 2025: 0, 2026: 1, 2027: 0.5 }
  ];

  let cumulativeProfitForBreakEven = 0;
  const breakEvenData = data.map(item => {
    cumulativeProfitForBreakEven += item.profit;
    return {
      year: item.year,
      cumulativeProfit: parseFloat(cumulativeProfitForBreakEven.toFixed(1))
    };
  });

  const calculateBreakEvenMonth = () => {
    if (breakEvenData[0].cumulativeProfit >= 0) return 0;
    for (let i = 1; i < breakEvenData.length; i++) {
      if (breakEvenData[i].cumulativeProfit >= 0) {
        const prevYear = breakEvenData[i-1];
        const currYear = breakEvenData[i];
        const profitDiff = currYear.cumulativeProfit - prevYear.cumulativeProfit;
        const negativeProfitPortion = Math.abs(prevYear.cumulativeProfit) / profitDiff;
        return 12 * (i-1) + Math.ceil(negativeProfitPortion * 12);
      }
    }
    return "Not within 3 years";
  };

  const breakEvenMonth = calculateBreakEvenMonth();

  return (
    <div className="bg-black p-4 rounded-lg text-purple-200">
      <h1 className="text-2xl font-bold text-center mb-6 text-purple-300">Financial ROI Analysis 2025-2027</h1>
      {/* Remaining JSX layout and charts remain unchanged */}
    </div>
  );
};

export default FinancialDashboard;
