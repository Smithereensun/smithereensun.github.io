{

  "title": "SpringBoot 对接美团闪购，检验签名，获取推送订单参数，text转json",
  "date": "2021-12-07",
  "description": "接口文档地址 订单推送(已确定订单)：https://open-shangou.meituan.com/home/docDetail/177 签名算法：https://opendj.meituan.com/home/questionDetail/5730 测试订单：https://opendj.me",
  "tags": [
    "Spring Boot"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/15657414.html"

}

# 接口文档地址

订单推送(已确定订单)：[https://open-shangou.meituan.com/home/docDetail/177](https://open-shangou.meituan.com/home/docDetail/177)

签名算法：[https://opendj.meituan.com/home/questionDetail/5730](https://opendj.meituan.com/home/questionDetail/5730)

测试订单：[https://opendj.meituan.com/platform/guide/market/10657](https://opendj.meituan.com/platform/guide/market/10657)

# 控制器

```text
    @RequestMapping("confirm_order")
    public void confirmOrder(HttpServletRequest request) {
        //验证美团闪购签名
        Boolean flag = CommonUtil.checkMeiTuanShanGouSign(request, "6bdfc78d4a64e82bc59e2a67d746a06e");
        if (flag) {
            SortedMap<String, String> requestParam = CommonUtil.getMeiTuanShanGouRequestParam(request);
            String json = JSON.toJSONString(requestParam);
            System.err.println(json);
            MeiTuanShanGouConfirmOrderVo vo = JSON.parseObject(json, MeiTuanShanGouConfirmOrderVo.class);
            System.out.println("=====================================");
            System.err.println(vo);
        }
    }
```

# 工具类

```text
 /**
     * 获取美团闪购请求参数
     *
     * @param request 请求头
     * @return
     */
    public static SortedMap<String, String> getMeiTuanShanGouRequestParam(HttpServletRequest request) {
        SortedMap<String, String> treeMap = new TreeMap<>();
        Enumeration<String> parameterNames = request.getParameterNames();
        while (parameterNames.hasMoreElements()) {
            String name = parameterNames.nextElement();
            String value = request.getParameter(name);
            if (!SIG_FIELD_NAME.equals(name)) {
                try {
                    treeMap.put(name, URLDecoder.decode(value, "UTF-8"));
                } catch (UnsupportedEncodingException e) {
                }
            }
        }
        return treeMap;
    }

    /**
     * 获取美团闪购签名
     *
     * @param url       请求url，注意不能带?，如：https://waimaiopen.meituan.com/api/v1/oauth/authorize
     * @param param     SortedMap<String, String> params = new TreeMap<>();
     * @param appSecret APP Secret
     * @return
     */
    public static String getMeiTuanShanGouSign(String url, SortedMap<String, String> param, String appSecret) {
        StringBuilder sb = new StringBuilder();
        Set<Map.Entry<String, String>> entries = param.entrySet();
        Iterator<Map.Entry<String, String>> it = entries.iterator();
        while (it.hasNext()) {
            Map.Entry<String, String> next = it.next();
            String key = next.getKey();
            String value = next.getValue();
            if (null != value && !"".equals(value) && !"sign".equals(key) && !"key".equals(key)) {
                sb.append(key + "=" + value + "&");
            }
        }
        String result = url + "?" + sb.substring(0, sb.toString().length() - 1) + appSecret;
        return MD5(result);
    }

    /**
     * 美团签名的字段名
     */
    private static final String SIG_FIELD_NAME = "sig";

    /**
     * 检查美团闪购签名
     *
     * @param request   请求头
     * @param appSecret 密钥
     * @return
     */
    public static Boolean checkMeiTuanShanGouSign(HttpServletRequest request, String appSecret) {
        String url = String.format("%s://%s%s", request.getScheme(), request.getServerName(), request.getRequestURI());
        SortedMap<String, String> treeMap = new TreeMap<>();
        Enumeration<String> parameterNames = request.getParameterNames();
        while (parameterNames.hasMoreElements()) {
            String name = parameterNames.nextElement();
            String value = request.getParameter(name);
            if (!SIG_FIELD_NAME.equals(name)) {
                try {
                    treeMap.put(name, URLDecoder.decode(value, "UTF-8"));
                } catch (UnsupportedEncodingException e) {
                }
            }
        }
        String sign = generatorMeiTuanShanGouSign(url, treeMap, appSecret);
        String realSign = request.getParameter(SIG_FIELD_NAME).toUpperCase();
        if (sign.equals(realSign)) {
            log.info("验证美团闪购签名正确，真实签名：{}", realSign);
            return true;
        }
        log.error("验证美团闪购签名错误，真实签名：{}", realSign);
        return false;
    }

    /**
     * 生成美团闪购签名
     *
     * @param url       请求的完整的url
     * @param treeMap   请求的全部参数
     * @param appSecret APP Secret
     * @return sign
     */
    private static String generatorMeiTuanShanGouSign(String url, SortedMap<String, String> treeMap, String appSecret) {
        String queryString = Joiner.on("&").useForNull("").withKeyValueSeparator("=").join(treeMap);
        String md5str = url.concat("?").concat(queryString).concat(appSecret);
        try {
            return MD5(URLDecoder.decode(md5str, "UTF-8"));
        } catch (UnsupportedEncodingException encodingException) {
            System.out.println("签名生成失败");
        }
        return "";
    }

    /**
     * md5加密
     *
     * @param data
     * @return
     */
    public static String MD5(String data) {
        try {
            java.security.MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] array = md.digest(data.getBytes("UTF-8"));
            StringBuilder sb = new StringBuilder();
            for (byte item : array) {
                sb.append(Integer.toHexString((item & 0xFF) | 0x100).substring(1, 3));
            }
            return sb.toString().toUpperCase();
        } catch (Exception exception) {
        }
        return null;
    }
```
