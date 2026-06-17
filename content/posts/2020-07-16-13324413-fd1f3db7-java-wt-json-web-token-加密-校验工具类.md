{

  "title": "java WT -- JSON WEB TOKEN 加密/校验工具类",
  "date": "2020-07-16",
  "description": "依赖项 JWTUtils.java",
  "tags": [
    "JWT"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13324413.html"

}

## 依赖项

```text
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt</artifactId>
            <version>0.7.0</version>
        </dependency>
```

## JWTUtils.java

```text
package net.ybclass.online_ybclass.utils;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import net.ybclass.online_ybclass.domain.User;

import java.util.Date;

/**
 * JWT工具类
 * 注意点：
 * 1、生成的token，是可以通过base64进行解密出铭文信息
 * 2、base64进行解密出明文信息，修改再进行编码，则会解密失败
 * 3、无法作废已颁布的token，除非改密钥
 */
public class JWTUtils {
    /**
     * 过期时间，一周
     */
    static final long EXPIRE = 60000 * 60 * 24 * 7;
    /**
     * 加密密钥
     */
    private static final String SECRET = "ybclass.net168";
    /**
     * 令牌前缀
     */
    private static final String TOKEN_PREFIX = "ybclass";
    /**
     * 主题
     */
    private static final String SUBJECT = "ybclass";

    /**
     * 根据用户信息，生成令牌
     *
     * @param user
     * @return
     */
    public static String geneJsonWebToken(User user) {
        String token = Jwts.builder().setSubject(SUBJECT)
                .claim("head_img", user.getHeadImg())
                .claim("id", user.getId())
                .claim("name", user.getName())
                .setIssuedAt(new Date()) //令牌颁布时间
                .setExpiration(new Date(System.currentTimeMillis() + EXPIRE)) //过期时间
                .signWith(SignatureAlgorithm.HS256, SECRET) //加密方式
                .compact();
        token = TOKEN_PREFIX + token;
        return token;
    }

    /**
     * 校验token方法
     *
     * @param token
     * @return
     */
    public static Claims checkJWT(String token) {
        try {
            final Claims claims = Jwts.parser()
                    .setSigningKey(SECRET)
                    .parseClaimsJws(token.replace(TOKEN_PREFIX, ""))
                    .getBody();
            return claims;
        } catch (Exception e) {
            return null;
        }
    }
}
```
