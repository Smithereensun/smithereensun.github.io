---
title: "Java List对象分组"
date: 2020-08-13
description: "实体类 必须重写equals和hashCode方法 package com.zcsoft.rc.backend.biz.vo.securityLibary; import java.util.Date; import java.util.Objects; /** * @ClassName：Secur"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13496104.html"
---

<h1>实体类</h1>
<p>　　<strong><span style="color: rgba(255, 0, 0, 1)">必须重写equals和hashCode方法</span></strong></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.zcsoft.rc.backend.biz.vo.securityLibary;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.Date;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.Objects;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * @ClassName：SecurityLibraryImportDistinctVO
 * @Description：安全风险库导入数据分组，根据导入数据分主表数据
 * @Author：chenyb
 * @Date：2020/8/13 11:30 上午
 * @Versiion：1.0
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> SecurityLibraryImportDistinctVO {
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 内码
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String id;
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 风险类别
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String riskType;
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 风险名称
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String riskName;
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 风险点
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String riskPoint;
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 风险点里程
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String riskPointMileage;
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 安全风险点描述
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String riskDesc;
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 可能造成的后果
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String causeResult;
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 风险等级
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String riskLevel;
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 风险期限
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> Date riskPeriod;
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 创建时间
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> Date createTime;
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 修改时间
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> Date modifyTime;
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getRiskType() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> riskType;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setRiskType(String riskType) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.riskType =<span style="color: rgba(0, 0, 0, 1)"> riskType;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getRiskName() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> riskName;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setRiskName(String riskName) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.riskName =<span style="color: rgba(0, 0, 0, 1)"> riskName;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getRiskPoint() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> riskPoint;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setRiskPoint(String riskPoint) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.riskPoint =<span style="color: rgba(0, 0, 0, 1)"> riskPoint;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getRiskPointMileage() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> riskPointMileage;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setRiskPointMileage(String riskPointMileage) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.riskPointMileage =<span style="color: rgba(0, 0, 0, 1)"> riskPointMileage;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getRiskDesc() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> riskDesc;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setRiskDesc(String riskDesc) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.riskDesc =<span style="color: rgba(0, 0, 0, 1)"> riskDesc;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getCauseResult() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> causeResult;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setCauseResult(String causeResult) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.causeResult =<span style="color: rgba(0, 0, 0, 1)"> causeResult;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getRiskLevel() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> riskLevel;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setRiskLevel(String riskLevel) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.riskLevel =<span style="color: rgba(0, 0, 0, 1)"> riskLevel;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Date getRiskPeriod() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> riskPeriod;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setRiskPeriod(Date riskPeriod) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.riskPeriod =<span style="color: rgba(0, 0, 0, 1)"> riskPeriod;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getId() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> id;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setId(String id) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.id =<span style="color: rgba(0, 0, 0, 1)"> id;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Date getCreateTime() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> createTime;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setCreateTime(Date createTime) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.createTime =<span style="color: rgba(0, 0, 0, 1)"> createTime;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Date getModifyTime() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> modifyTime;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setModifyTime(Date modifyTime) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.modifyTime =<span style="color: rgba(0, 0, 0, 1)"> modifyTime;
    }

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String toString() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> "SecurityLibraryImportDistinctVO{" +
                "id='" + id + '\'' +
                ", riskType='" + riskType + '\'' +
                ", riskName='" + riskName + '\'' +
                ", riskPoint='" + riskPoint + '\'' +
                ", riskPointMileage='" + riskPointMileage + '\'' +
                ", riskDesc='" + riskDesc + '\'' +
                ", causeResult='" + causeResult + '\'' +
                ", riskLevel='" + riskLevel + '\'' +
                ", riskPeriod=" + riskPeriod +
                ", createTime=" + createTime +
                ", modifyTime=" + modifyTime +
                '}'<span style="color: rgba(0, 0, 0, 1)">;
    }

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">boolean</span><span style="color: rgba(0, 0, 0, 1)"> equals(Object o) {
        </span><span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">this</span> == o) <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
        </span><span style="color: rgba(0, 0, 255, 1)">if</span> (!(o <span style="color: rgba(0, 0, 255, 1)">instanceof</span> SecurityLibraryImportDistinctVO)) <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">;
        SecurityLibraryImportDistinctVO that </span>=<span style="color: rgba(0, 0, 0, 1)"> (SecurityLibraryImportDistinctVO) o;
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> Objects.equals(riskType, that.riskType) &amp;&amp;<span style="color: rgba(0, 0, 0, 1)">
                Objects.equals(riskName, that.riskName) </span>&amp;&amp;<span style="color: rgba(0, 0, 0, 1)">
                Objects.equals(riskPoint, that.riskPoint) </span>&amp;&amp;<span style="color: rgba(0, 0, 0, 1)">
                Objects.equals(riskPointMileage, that.riskPointMileage) </span>&amp;&amp;<span style="color: rgba(0, 0, 0, 1)">
                Objects.equals(riskDesc, that.riskDesc) </span>&amp;&amp;<span style="color: rgba(0, 0, 0, 1)">
                Objects.equals(causeResult, that.causeResult) </span>&amp;&amp;<span style="color: rgba(0, 0, 0, 1)">
                Objects.equals(riskLevel, that.riskLevel) </span>&amp;&amp;<span style="color: rgba(0, 0, 0, 1)">
                Objects.equals(riskPeriod, that.riskPeriod);
    }

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> hashCode() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> Objects.hash(riskType, riskName, riskPoint, riskPointMileage, riskDesc, causeResult, riskLevel, riskPeriod);
    }
}</span></pre>
