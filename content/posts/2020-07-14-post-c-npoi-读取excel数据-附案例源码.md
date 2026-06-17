---
title: "C# NPOI 读取Excel数据，附案例源码"
date: 2020-07-14
description: "项目结构 注意：需要引入NPOI类库 C#代码 Form1.cs using NPOI.HSSF.UserModel; using NPOI.SS.UserModel; using System; using System.Collections.Generic; using System.Comp"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13300297.html"
---

<h1 style="text-align: center">项目结构</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200714172419563-409118260.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>注意：需要引入NPOI类库</strong></span></p>
<h1 style="text-align: center">C#代码</h1>
<h2>Form1.cs</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> NPOI.HSSF.UserModel;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> NPOI.SS.UserModel;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Collections.Generic;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.ComponentModel;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Data;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Drawing;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.IO;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Linq;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Text;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Threading.Tasks;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Windows.Forms;

</span><span style="color: rgba(0, 0, 255, 1)">namespace</span><span style="color: rgba(0, 0, 0, 1)"> NPOIDemo
{
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">partial</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Form1 : Form
    {
        </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Form1()
        {
            InitializeComponent();
        }
        </span><span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">const</span> <span style="color: rgba(0, 0, 255, 1)">int</span> DEFAULT_CHECK_CELL_NUM = <span style="color: rgba(128, 0, 128, 1)">4</span><span style="color: rgba(0, 0, 0, 1)">;
        </span><span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">void</span> button1_Click(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> sender, EventArgs e)
        {
            </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)">
            {
                DataTable dt</span>=ReadExcelData(<span style="color: rgba(128, 0, 0, 1)">@"</span><span style="color: rgba(128, 0, 0, 1)">C:\Users\apple\Desktop\Test.xls</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
                MessageBox.Show(</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ok</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
            }
            </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
           
        }
        </span><span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 读取Excel中数据
        </span><span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="filePath"&gt;&lt;/param&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">private</span> DataTable ReadExcelData(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> filePath)
        {
            </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)">
            {
                </span><span style="color: rgba(0, 0, 255, 1)">if</span> (!<span style="color: rgba(0, 0, 0, 1)">File.Exists(filePath.ToString()))
                {
                    </span><span style="color: rgba(0, 0, 255, 1)">throw</span> <span style="color: rgba(0, 0, 255, 1)">new</span> Exception(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">文件不存在!</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
                }
                DataTable dtExcel </span>=<span style="color: rgba(0, 0, 0, 1)"> InitDataTable();
                FileStream fsRead </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> FileStream(filePath.ToString(), FileMode.Open);
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">创建工作薄</span>
                IWorkbook workBook = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> HSSFWorkbook(fsRead);
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">获取Sheet</span>
                ISheet sheet = workBook.GetSheetAt(<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">);
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">获取Excel中的行数</span>
                <span style="color: rgba(0, 0, 255, 1)">int</span> ExcelRowsCount =<span style="color: rgba(0, 0, 0, 1)"> sheet.LastRowNum;
                Assert.IsTrue(ExcelRowsCount </span>== <span style="color: rgba(128, 0, 128, 1)">1</span>, <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">未读到Excel数据!</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
                IRow currentRow;
                DataRow dr;
                </span><span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">int</span> i = <span style="color: rgba(128, 0, 128, 1)">1</span>; i &lt; ExcelRowsCount; i++<span style="color: rgba(0, 0, 0, 1)">)
                {
                    dr </span>=<span style="color: rgba(0, 0, 0, 1)"> dtExcel.NewRow();
                    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">当前行数据</span>
                    currentRow =<span style="color: rgba(0, 0, 0, 1)"> sheet.GetRow(i);
                    SetCurrentRowValue(dtExcel, dr, currentRow, currentRow.LastCellNum);
                }
                </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> dtExcel;
            }
            </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
            {
                </span><span style="color: rgba(0, 0, 255, 1)">throw</span><span style="color: rgba(0, 0, 0, 1)"> ex;
            }
        }
        </span><span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 初始化DataTable
        </span><span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> DataTable InitDataTable()
        {
            DataTable dt_excel </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> DataTable();
            dt_excel.Columns.Add(</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">A</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
            dt_excel.Columns.Add(</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">B</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
            dt_excel.Columns.Add(</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">C</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
            dt_excel.Columns.Add(</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">D</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
            </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> dt_excel;
        }
        </span><span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 读取到的Excel的单元格数量
        </span><span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="currentCellNum"&gt;&lt;/param&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">void</span> CheckExcelCellNum(<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> readCurrentRowCellNum)
        {
            Assert.IsTrue(readCurrentRowCellNum </span>&gt; DEFAULT_CHECK_CELL_NUM, <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Excel单元格列数超过：</span><span style="color: rgba(128, 0, 0, 1)">"</span>+DEFAULT_CHECK_CELL_NUM+<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">列</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
        }
        </span><span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 给DataTable动态赋值
        </span><span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="dr"&gt;</span><span style="color: rgba(0, 128, 0, 1)">DataTable当前行</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="currentRow"&gt;</span><span style="color: rgba(0, 128, 0, 1)">Excel当前行数据</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="currentCellNum"&gt;</span><span style="color: rgba(0, 128, 0, 1)">Excel的列数</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">void</span> SetCurrentRowValue(DataTable dtExcel, DataRow dr,IRow currentRow, <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> currentCellNum)
        {
            dr.BeginEdit();
            </span><span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">int</span> j = <span style="color: rgba(128, 0, 128, 1)">0</span>; j &lt; currentCellNum; j++<span style="color: rgba(0, 0, 0, 1)">)
            {
                </span><span style="color: rgba(0, 0, 255, 1)">if</span> (j &gt;= DEFAULT_CHECK_CELL_NUM) <span style="color: rgba(0, 0, 255, 1)">break</span><span style="color: rgba(0, 0, 0, 1)">;
                dr[j]</span>=<span style="color: rgba(0, 0, 0, 1)"> currentRow.GetCell(j).ToString().Trim();
            }
            dr.EndEdit();
            dtExcel.Rows.Add(dr);
        }
    }
}</span></pre>
