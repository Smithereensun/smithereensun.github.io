{

  "title": "C# NPOI 读取Excel数据，附案例源码",
  "date": "2020-07-14",
  "description": "项目结构 注意：需要引入NPOI类库** C#代码 Form1.cs Assert.cs 演示 演示过程中，提示另外一个进程xxxx的，是因为NPOI读取Excel的时候，Excel不可以打开，我们关闭，然后再次执行即可 项目下载",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13300297.html"

}

# 项目结构

![](./images/images/img_001_4b059755de16.png)

**注意：需要引入NPOI类库**

# C#代码

## Form1.cs

```text
using NPOI.HSSF.UserModel;
using NPOI.SS.UserModel;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace NPOIDemo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private const int DEFAULT_CHECK_CELL_NUM = 4;
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                DataTable dt=ReadExcelData(@"C:\Users\apple\Desktop\Test.xls");
                MessageBox.Show("ok");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

        }
        /// <summary>
        /// 读取Excel中数据
        /// </summary>
        /// <param name="filePath"></param>
        private DataTable ReadExcelData(object filePath)
        {
            try
            {
                if (!File.Exists(filePath.ToString()))
                {
                    throw new Exception("文件不存在!");
                }
                DataTable dtExcel = InitDataTable();
                FileStream fsRead = new FileStream(filePath.ToString(), FileMode.Open);
                //创建工作薄
                IWorkbook workBook = new HSSFWorkbook(fsRead);
                //获取Sheet
                ISheet sheet = workBook.GetSheetAt(0);
                //获取Excel中的行数
                int ExcelRowsCount = sheet.LastRowNum;
                Assert.IsTrue(ExcelRowsCount == 1, "未读到Excel数据!");
                IRow currentRow;
                DataRow dr;
                for (int i = 1; i < ExcelRowsCount; i++)
                {
                    dr = dtExcel.NewRow();
                    //当前行数据
                    currentRow = sheet.GetRow(i);
                    SetCurrentRowValue(dtExcel, dr, currentRow, currentRow.LastCellNum);
                }
                return dtExcel;
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }
        /// <summary>
        /// 初始化DataTable
        /// </summary>
        /// <returns></returns>
        private DataTable InitDataTable()
        {
            DataTable dt_excel = new DataTable();
            dt_excel.Columns.Add("A");
            dt_excel.Columns.Add("B");
            dt_excel.Columns.Add("C");
            dt_excel.Columns.Add("D");
            return dt_excel;
        }
        /// <summary>
        /// 读取到的Excel的单元格数量
        /// </summary>
        /// <param name="currentCellNum"></param>
        private void CheckExcelCellNum(int readCurrentRowCellNum)
        {
            Assert.IsTrue(readCurrentRowCellNum > DEFAULT_CHECK_CELL_NUM, "Excel单元格列数超过："+DEFAULT_CHECK_CELL_NUM+"列");
        }
        /// <summary>
        /// 给DataTable动态赋值
        /// </summary>
        /// <param name="dr">DataTable当前行</param>
        /// <param name="currentRow">Excel当前行数据</param>
        /// <param name="currentCellNum">Excel的列数</param>
        private void SetCurrentRowValue(DataTable dtExcel, DataRow dr,IRow currentRow, int currentCellNum)
        {
            dr.BeginEdit();
            for (int j = 0; j < currentCellNum; j++)
            {
                if (j >= DEFAULT_CHECK_CELL_NUM) break;
                dr[j]= currentRow.GetCell(j).ToString().Trim();
            }
            dr.EndEdit();
            dtExcel.Rows.Add(dr);
        }
    }
}
```

## Assert.cs

```text
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NPOIDemo
{
    public static class Assert
    {
        public static void IsTrue(bool flag,string msg)
        {
            if (flag)
            {
                throw new Exception(msg);
            }
        }
    }
}
```

## 演示

![](./images/images/img_002_4b88d4820542.gif)

　　演示过程中，提示另外一个进程xxxx的，是因为NPOI读取Excel的时候，Excel不可以打开，我们关闭，然后再次执行即可

## 项目下载

```text
链接：https://pan.baidu.com/s/1YLer2fgV6QhJIQVsxqozJQ
提取码：30a9
```
